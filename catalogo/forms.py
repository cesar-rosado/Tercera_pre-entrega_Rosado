from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    telefono = forms.IntegerField()
    direccion= forms.CharField(max_length=256)