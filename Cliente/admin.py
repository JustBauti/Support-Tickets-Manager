from django.contrib import admin

from .models import Cliente
from django.core.mail import send_mail




# Register your models here.
@admin.register(Cliente)
class Clientedate(admin.ModelAdmin):
    list_display = ("nombre_apellido", "codigo")
    search_fields_name =("filtro")
    search_fields = ("nombre_apellido__startswith","codigo__startswith","estado__startswith")

    def save_model(self, request, obj, form, change):
        cliente = Cliente.objects.filter(id=obj.id)
        super().save_model(request, obj, form, change)

    change_form_template = "./admin/Cliente/form_change.html"
