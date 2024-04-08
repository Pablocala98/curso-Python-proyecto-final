from django.db import models
from django.utils import timezone

# Create your models here.

from django.db import models
    
class Consultorio(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {'Disponible' if self.disponible else 'No Disponible'} - Capacidad: {self.capacidad}"
    
class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    duracion = models.IntegerField(default=1)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.consultorio.nombre} - {self.fecha}"

