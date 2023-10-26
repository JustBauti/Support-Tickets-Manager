from django.db import models

# Create your models here.
EstadoOpciones  = (
 ('En produccion','En produccion'),
 ('Listo para retirar','Listo para retirar'),
 ('Aceptado','Aceptado'),

)
class Cliente(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    nombre_apellido = models.CharField("Nombre y Apellido",max_length=150)
    correo = models.EmailField("Correo electronico",max_length=254)
    problema = models.TextField("Problema con el dispositivo",max_length=1000)
    estado = models.CharField("Estado en el que se encuentra el pedido",choices=EstadoOpciones, max_length=20)
    codigo = models.CharField("Codigo de seguimiento",default= 1, max_length=50)
    
    def data(self):
        return {
            "nombres":self.nombre_apellido,
            "problema":self.problema,
            "estado":self.estado,
            "codigo":self.codigo,
            "correo":self.correo
        }
    
    def __str__(self):
        return self.nombre_apellido