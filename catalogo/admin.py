from django.contrib import admin

from catalogo.models import Cliente, Computadora, Accesorio, Proveedor
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Computadora)
admin.site.register(Accesorio)
admin.site.register(Proveedor)