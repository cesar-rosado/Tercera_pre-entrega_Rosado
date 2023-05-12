from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(required=False)
    telefono = forms.IntegerField()
    direccion= forms.CharField(max_length=256)

class ComputadoraFormulario(forms.Form):
    tipo_computadora = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    procesador = forms.CharField(max_length=20)
    ram = forms.IntegerField(required=False)
    hhd = forms.IntegerField(required=False)
    
class AccesorioFormulario(forms.Form):
    tipo_accesorio = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    
class ProveedorFormulario(forms.Form):
    empresa = forms.CharField(max_length=256)
    direccion = forms.CharField(max_length=256, required=False)
    email = forms.EmailField()
    telefono = forms.IntegerField(required=False)