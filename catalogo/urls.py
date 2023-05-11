from django.contrib import admin
from django.urls import path

from catalogo.views import listar_clientes, listar_computadoras, listar_accesorios, listar_proveedores

urlpatterns = [
    path("clientes/", listar_clientes, name="clientes"),
    path("computadoras/", listar_computadoras, name="computadoras"),
    path("accesorios/", listar_accesorios, name="accesorios"),
    path("proveedores/", listar_proveedores, name="proveedores"),      
]