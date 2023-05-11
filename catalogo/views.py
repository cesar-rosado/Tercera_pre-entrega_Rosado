from django.shortcuts import render, redirect
from django.urls import reverse

from catalogo.models import Cliente, Computadora, Accesorio, Proveedor

# Create your views here.

def listar_clientes(resquest):
    contexto = {
        "clientes": Cliente.objects.all(),
    }
    
    http_response = render(
        request=resquest,
        template_name='catalogo/clientes.html',
        context = contexto,
    )
    return http_response

def listar_computadoras(resquest):
    contexto = {
        "computadora": Computadora.objects.all(),
    }
    
    http_response = render(
        request=resquest,
        template_name='catalogo/computadoras.html',
        context = contexto,
    )
    return http_response

def listar_accesorios(resquest):
    contexto = {
        "accesorio": Accesorio.objects.all(),
    }
    
    http_response = render(
        request=resquest,
        template_name='catalogo/accesorios.html',
        context = contexto,
    )
    return http_response

def listar_proveedores(resquest):
    contexto = {
        "proveedor": Proveedor.objects.all(),
    }
    
    http_response = render(
        request=resquest,
        template_name='catalogo/proveedores.html',
        context = contexto,
    )
    return http_response
