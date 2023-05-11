from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='catalogo/index.html',
        context=contexto,
    )
    return http_response


###########################################################################################################################################################

def saludar(request): #Funcion de prueba
    saludo = "Hola usuario bienvenido a la pagina de prueba"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request): #Funcion de prueba
    contexto = {}
    http_response = render(
        request=request,
        template_name='catalogo/base.html',
        context=contexto,
    )
    return http_response