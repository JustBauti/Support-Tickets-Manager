from django import forms
from django.contrib import admin
from .models import Servicio, Tecnico
from django.utils.html import format_html
from django.http import HttpResponseRedirect

class ServiciosAdminForm(forms.ModelForm):
    fecha_deja_prod = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        input_formats=['%d/%m/%Y %H:%M']  # La fecha y hora deben ingresarse en este formato
    )

    fecha_terminacion_prod = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        input_formats=['%d/%m/%Y %H:%M']  # La fecha y hora deben ingresarse en este formato
    )

    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'tipo_reparacion': forms.RadioSelect
        }

@admin.register(Servicio)
class Serviciosdate(admin.ModelAdmin):
    form = ServiciosAdminForm
    actions = ['mostrar_todos', 'excluir_entregados']
    list_display = ("nombre_apellido", "estado_color", "fecha_entrada", "fecha_termina","codigo")
    search_fields = ("nombre_apellido__startswith","estado__startswith")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if 'excluir_entregados' in request.session:
            qs = qs.exclude(estado='ENTREGADO')
        return qs

    # def mostrar_todos(self, request, queryset):
    #     if 'excluir_entregados' in request.session:
    #         del request.session['excluir_entregados']
    #     self.message_user(request, "Ahora se muestran todos los objetos.")
    #     return HttpResponseRedirect(request.get_full_path())
    # mostrar_todos.short_description = "Mostrar todos los objetos"

    # def excluir_entregados(self, request, queryset):
    #     request.session['excluir_entregados'] = True
    #     self.message_user(request, "Se excluyeron los objetos con estado 'ENTREGADO'.")
    #     return HttpResponseRedirect(request.get_full_path())
    # excluir_entregados.short_description = "Excluir objetos con estado 'ENTREGADO'"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if 'excluir_entregados' in request.session:
            qs = qs.exclude(estado='ENTREGADO')
        return qs

    def mostrar_todos(self, request, queryset):
        if 'excluir_entregados' in request.session:
            del request.session['excluir_entregados']
        self.message_user(request, "Ahora se muestran todos los objetos.")
        return HttpResponseRedirect(request.get_full_path())
    mostrar_todos.short_description = "Mostrar todos los objetos"
    mostrar_todos.acts_on_all = True

    def excluir_entregados(self, request, queryset):
        request.session['excluir_entregados'] = True
        self.message_user(request, "Se excluyeron los objetos con estado 'ENTREGADO'.")
        return HttpResponseRedirect(request.get_full_path())
    excluir_entregados.short_description = "Excluir objetos con estado 'ENTREGADO'"
    excluir_entregados.acts_on_all = True   

    def estado_color(self, obj):
        colores = {
            'Aceptado': '#0000FF',  # Azul
            'Listo para retirar': '#008000',  # Verde
            'No se puede arreglar': '#FF0000',  # Rojo
            'En Arreglo': '#FFA500',  # Naranja
        }
        color = colores.get(obj.estado, '#000000')
        return format_html('<span style="color: {};">{}</span>', color, obj.estado)
    estado_color.short_description = 'estado'
    estado_color.admin_order_field = 'estado'

    def fecha_entrada(self, obj):
        return obj.fecha_deja_prod.strftime('%d/%m/%y - %H:%M hs')  
    fecha_entrada.admin_order_field = 'fecha_deja_prod'

    def fecha_termina(self, obj):
        return obj.fecha_terminacion_prod.strftime('%d/%m/%y - %H:%M hs')
    fecha_termina.admin_order_field = 'fecha_terminacion_prod'
 

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    change_form_template = 'admin/Servicios/form_change.html'

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        ultimo_cliente = Servicio.objects.order_by('id').last()
        if ultimo_cliente:
            # Si hay un último cliente, se toma su ID, se le suma 1000 y se asigna al próximo cliente
            extra_context['codigo_cliente'] = str(ultimo_cliente.id + 1000)
        else:
            # Si no hay clientes, se asigna el código 1000 al primer cliente
            extra_context['codigo_cliente'] = '1000'
        print("add_view se está ejecutando, codigo_cliente es: ", extra_context['codigo_cliente'])
        return super().add_view(request, form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # Get the current Servicio object
        servicio = Servicio.objects.get(id=object_id)
        # Add the codigo_cliente to the context
        extra_context['codigo_cliente'] = servicio.codigo
        extra_context['object_id'] = object_id
        print(object_id)
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

@admin.register(Tecnico)
class Tecnicos(admin.ModelAdmin):
    change_form_template = "./admin/Tecnicos/form_change.html"