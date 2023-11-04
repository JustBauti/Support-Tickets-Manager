from django import forms
from django.contrib import admin
from .models import Cliente

class ClienteAdminForm(forms.ModelForm):
    fecha_deja_prod = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        input_formats=['%d/%m/%Y %H:%M']  # La fecha y hora deben ingresarse en este formato
    )

    fecha_terminacion_prod = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        input_formats=['%d/%m/%Y %H:%M']  # La fecha y hora deben ingresarse en este formato
    )

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'tipo_reparacion': forms.RadioSelect
        }

@admin.register(Cliente)
class Clientedate(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ("nombre_apellido", "estado", "fecha_entrada", "fecha_termina","codigo")
    search_fields = ("nombre_apellido__startswith","estado__startswith")

    def fecha_entrada(self, obj):
        return obj.fecha_deja_prod.strftime('%d/%m/%y - %H:%M hs')  
    fecha_entrada.admin_order_field = 'fecha_deja_prod'

    def fecha_termina(self, obj):
        return obj.fecha_terminacion_prod.strftime('%d/%m/%y - %H:%M hs')
    fecha_termina.admin_order_field = 'fecha_terminacion_prod'
 

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    change_form_template = "./admin/Cliente/form_change.html"