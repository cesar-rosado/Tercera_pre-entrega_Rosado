from django.contrib import admin
from django.urls import path

from catalogo.views import listar_clientes, listar_computadoras, listar_accesorios, listar_proveedores, crear_cliente, buscar_cliente

urlpatterns = [
    path("clientes/", listar_clientes, name="clientes"),
    path("crear-cliente/", crear_cliente, name="crear_cliente"),
    path("buscar-cliente/", buscar_cliente, name="buscar_cliente"),
    path("computadoras/", listar_computadoras, name="computadoras"),
    path("accesorios/", listar_accesorios, name="accesorios"),
    path("proveedores/", listar_proveedores, name="proveedores"),      
]