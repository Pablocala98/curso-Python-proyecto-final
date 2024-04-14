from django import forms
from .models import Consultorio



class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")

class ReservaCreateForm(forms.Form):
    pass

class ConsultorioCreateForm(forms.ModelForm):
    class Meta:
        model = Consultorio
        fields = ['nombre','disponible','capacidad','descripcion']
        labels = {
            'nombre': 'Elegir un nombre para la Sala',
            'disponible': 'Disponible',
            'capacidad': 'Capacidad máxima',
            'descripcion': 'Descripción',
        }