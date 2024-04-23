from django import forms
from .models import Consultorio, Reserva, Masajista
from django.contrib.auth.models import User



class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")

class ConsultorioSearchForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Ingresar nombre de Consultorio")

class MasajistaSearchForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Ingresar nombre de Masajista")

class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_de_usuario', 'consultorio', 'fecha', 'hora', 'duracion', 'descripcion']
        labels = {
            'nombre_de_usuario': 'Nombre del Usuario',
            'consultorio': 'Consultorio',
            'fecha': 'Fecha de la Reserva',
            'hora': 'Hora de la Reserva',
            'duracion': 'Duración (en horas)',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre_de_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Usuario'}),
            'consultorio': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 12}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la reserva'}),
        }

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
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del consultorio'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del consultorio'}),
        }

class MasajistaCreateForm(forms.ModelForm):
    class Meta:
        model = Masajista
        fields = ['nombre','apellido','documento','telefono']
        labels = {
            'nombre': 'Nombre del Masajista',
            'apellido': 'Apellido',
            'documento': 'Documento',
            'telefono': 'Telefono',
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']