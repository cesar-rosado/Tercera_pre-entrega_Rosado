from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(blank=True)
    telefono = models.IntegerField(blank=True)
    direccion= models.CharField(max_length=256, blank=True)
    
    def __str__(self):
        return f"{self.nombre}  {self.apellido}"
    
class Computadora(models.Model):
    tipo_computadora = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    procesador = models.CharField(max_length=20)
    ram = models.IntegerField(blank=True)
    hhd = models.IntegerField(blank=True)
    
    def __str__(self):
        return f"{self.tipo_computadora} | {self.marca} | {self.modelo}"
    
class Accesorio(models.Model):
    tipo_accesorio = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.tipo_accesorio} | {self.marca} | {self.modelo}"

class Proveedor(models.Model):
    empresa = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256, blank=True)
    email = models.EmailField()
    telefono = models.IntegerField(blank=True)
    
    def __str__(self):
        return f"{self.empresa}"