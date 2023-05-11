from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    direccion= models.CharField(max_length=256)
    
class Computadora(models.Model):
    tipo_computadora = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    procesador = models.CharField(max_length=20)
    ram = models.IntegerField()
    hhd = models.IntegerField()
    
class Accesorio(models.Model):
    tipo_accesorio = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)

class Proveedor(models.Model):
    empresa = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.IntegerField()