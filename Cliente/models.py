from random import choice
from django.db import models
import django.utils.timezone 

# Create your models here.

EstadoOpciones  = (
 ('En produccion','En produccion'),
 ('Listo para retirar','Listo para retirar'),
 ('Aceptado','Aceptado'),
)

reparacionOpciones  = (
 ('Reparacion por garantia','Reparacion por garantia'),
 ('reparacion por cuenta del cliente','reparacion por cuenta del cliente'),

)

class Cliente(models.Model):

    def generar():
        c = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join([choice(c) for i in range(10)])

    id = models.AutoField(primary_key=True, unique=True)
    # ORDEN DE RECEPCION
    codigo = models.CharField("codigo de seguimiento", default=generar(), max_length=10, blank=True, null=True)
    fecha_deja_prod = models.DateTimeField("Fecha entrada", default=django.utils.timezone.now, editable=True, blank=False)
    nombre_apellido = models.CharField("Nombre y Apellido", max_length=126, default="", blank=False, null=True)
    telefono_contacto = models.CharField(("Telefono de contacto"), default="+54", max_length=40, blank=True, null=True)
    direccion = models.CharField("Direccion", max_length=256, default="", blank=True, null=True)
    email = models.EmailField("Correo electronico", max_length=254, default="", blank=True, null=True)
    equipo = models.CharField("Equipo", max_length=126, default="", blank=True, null=True)
    marca_equipo = models.CharField("Marca del equipo", max_length=126, default="", blank=True, null=True)
    modelo_equipo = models.CharField("Modelo del equipo", max_length=126, default="", blank=True, null=True)
    numero_serie = models.CharField("Numero de serie del equipo", max_length=126, default="", blank=True, null=True)
    imei = models.IntegerField("Imei del equipo", default=0, blank=True, null=True)
    descripcion_problema = models.TextField(("Breve descripcion del problema"), max_length=512, default="", blank=True, null=True)

    # TIPO DE REPARACION
    tipo_reparacion = models.CharField("tipo de reparacion", choices=reparacionOpciones, default="", max_length=200, blank=True, null=True )    

    # DETALLES DEL PRODUCTO
    fisuras = models.CharField("Fisuras/Quebraduras", max_length=150, default = "", blank=True, null=True)
    pintura = models.CharField("Pintura dañada", max_length=150, default = "", blank=True, null=True)
    marcas = models.CharField("Marcas/Rayones", max_length=150, default = "", blank=True, null=True)
    golpes_graves = models.CharField("Golpes Graves", max_length=150, default = "", blank=True, null=True)
    manchas = models.CharField("Manchas", max_length=150, default = "", blank=True, null=True)
    golpes_leves= models.CharField("Golpes leves", max_length=150, default = "", blank=True, null=True)    
    componentes_faltantes = models.CharField("Componentes Faltantes", max_length=150, default = "", blank=True, null=True)
    otros = models.CharField("Otros", max_length=150, default = "", blank=True, null=True)

    #MAS DATOS SIN SECCION ESPECIFICA
    observaciones = models.TextField(("Otras Observaciones"), max_length=512, default="", blank=True, null=True)
    objectos = models.CharField(("Objectos que deja"), max_length=512, default="", blank=True, null=True)
    fecha_terminacion_prod = models.DateTimeField("Fecha Salida", editable=True, blank=False)
    monto_total = models.IntegerField("Monto total (Aprox)", default=0, blank=True, null=True)

    tecnico = models.CharField("Tecnico encargado", max_length=50, default="", blank=True, null=True)
    parte_pago = models.IntegerField("Pago por adelantado", default=0, blank=True, null=True)

    estado = models.CharField("Estado del pedido", choices=EstadoOpciones, max_length=20, blank=True, null=True)


    def get_data(self):
        return {
            "estado":self.estado,
            "montoTotal":self.monto_total,            
            "partePago":self.parte_pago,
            "finalizacion":self.fecha_terminacion_prod,
            "nombre":self.nombre_apellido,
            "problema":self.descripcion_problema

        }
    def __str__(self):
        return f"El usuario {self.nombre_apellido}"