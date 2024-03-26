from django.db import models

# Create your models here.

#class Reserva:
#    
#   def __init__(self, nombre_de_usuario, consultorio):
#        self.nombre_de_usuario = nombre_de_usuario
#        self.consultorio = consultorio
#
#    def __str__(self) -> str:
#        return f"Esta es una reserva a nombre de {self.nombre_de_usuario} para el consultorio {self.consultorio}"

class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length = 50)
    consultorio = models.CharField(max_length = 50)

    def __str__(self) -> str:
    
        return f"Esta es una reserva a nombre de {self.nombre_de_usuario} para el consultorio {self.consultorio}"

