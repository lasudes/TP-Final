from django import forms

class FormularioContacto (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()

