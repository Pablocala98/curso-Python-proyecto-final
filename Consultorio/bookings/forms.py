from django import forms

class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")
