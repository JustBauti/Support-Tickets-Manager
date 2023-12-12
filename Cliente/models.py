from django.db import models
import django.utils.timezone 

# Create your models here.

EstadoOpciones  = (
 ('En Arreglo','En Arreglo'),
 ('Listo para retirar','Listo para retirar'),
 ('Aceptado','Aceptado'),
 ('No se puede arreglar','No se puede arreglar')
)

reparacionOpciones  = (
 ('Reparacion por garantia','Reparacion por garantia'),
 ('reparacion por cuenta del cliente','reparacion por cuenta del cliente'),

)


class Tecnico(models.Model):
    nombre_apellido = models.CharField("Nombre del tecnico", max_length=500)
    
    def __str__(self):  # Método para personalizar la representación en cadena
        return self.nombre_apellido

class Servicio(models.Model):
    id = models.AutoField(primary_key=True, unique=True)

    # ORDEN DE RECEPCION
    codigo = models.CharField("codigo de seguimiento", default= "", max_length=100, blank=True, null=True)
    fecha_deja_prod = models.DateTimeField("Fecha entrada", default=django.utils.timezone.now, editable=True, blank=False)
    nombre_apellido = models.CharField("Nombre y Apellido", max_length=126, default="", blank=False, null=True)
    telefono_contacto = models.CharField(("Telefono de contacto"), default="+549", max_length=40, blank=True, null=True)
    equipo = models.CharField("Equipo", max_length=126, default="", blank=True, null=True)
    modelo_equipo = models.CharField("Modelo del equipo", max_length=126, default="", blank=True, null=True)
    imei = models.IntegerField("Imei del equipo", default=0, blank=True, null=True)
    descripcion_problema = models.TextField(("Breve descripcion del problema"), max_length=512, default="", blank=True, null=True)
    mensaje = models.TextField("Mensaje que se enviara", max_length=500, null= True)
    # TIPO DE REPARACION
    tipo_reparacion = models.CharField("tipo de reparacion", choices=reparacionOpciones, default="reparacion por cuenta del cliente", max_length=200, blank=False)    

    # DETALLES DEL PRODUCTO
    fisuras = models.BooleanField("Fisuras/Quebraduras",default=False )
    pintura = models.BooleanField("Pintura dañada",default=False )
    marcas = models.BooleanField("Marcas/Rayones",default=False )
    golpes_graves = models.BooleanField("Golpes Graves",default=False )
    manchas = models.BooleanField("Manchas",default=False )
    golpes_leves= models.BooleanField("Golpes leves",default=False )    
    otros = models.CharField("Otros", max_length=150, default = "", blank=True, null=True)

    #MAS DATOS SIN SECCION ESPECIFICA
    objectos = models.TextField(("Objectos que deja"), max_length=512, default="", blank=True, null=True)
    fecha_terminacion_prod = models.DateTimeField("Fecha Salida", editable=True, blank=False)
    monto_total = models.IntegerField("Monto total (Aprox)", default=0, blank=True, null=True)

    tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, blank=True, null=True)
    parte_pago = models.IntegerField("Pago por adelantado", default=0, blank=True, null=True)

    estado = models.CharField("Estado del pedido", choices=EstadoOpciones, default="Aceptado" , max_length=20, blank=True, null=True)
    dibujo_patron = models.IntegerField("Patron",default=0, blank=True)
    codigo_patron = models.CharField("Contrasena/Pin", default="",blank=True, max_length=100)




    def get_data(self):
        return {
            "estado":self.estado,
            "montoTotal":self.monto_total,            
            "partePago":self.parte_pago,
            "finalizacion":self.fecha_terminacion_prod,
            "nombre":self.nombre_apellido,
            "problema":self.descripcion_problema,
            "aPagar":self.monto_total - self.parte_pago,
            "codigo":self.codigo,
            "equipo":self.equipo,
            "modelo":self.modelo_equipo
        }
    def __str__(self):
        return f"El usuario {self.nombre_apellido}"
