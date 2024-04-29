from django.contrib import admin
from .models import Reserva, Consultorio, Masajista, Avatar

# Register your models here.

admin.site.register(Reserva)
admin.site.register(Consultorio)
admin.site.register(Masajista)
admin.site.register(Avatar)