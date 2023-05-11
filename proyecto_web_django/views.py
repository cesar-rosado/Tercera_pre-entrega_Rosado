from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo = "Hola usuario bienvenido a la pagina de prueba"
    pagina_html = HttpResponse(saludo)
    return pagina_html