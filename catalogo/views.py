from django.shortcuts import render, redirect
from django.urls import reverse

from catalogo.forms import ClienteFormulario, ComputadoraFormulario, AccesorioFormulario, ProveedorFormulario
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

########################################################################################################
#CREAR FORMULARIOS

def crear_cliente(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            email = data["email"]
            fecha_nacimiento = data["fecha_nacimiento"]
            telefono = data["telefono"]
            direccion= data["direccion"]
            cliente = Cliente(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, telefono=telefono, direccion=direccion)
            cliente.save()
            
            url_exitosa = reverse('clientes') 
            return redirect(url_exitosa)
               
    else: # GET
        formulario = ClienteFormulario()
    http_response = render(
        request=request,
        template_name='catalogo/formulario_clientes.html',
        context={'formulario' : formulario},
    )
    return http_response

def crear_computadora(request):
    if request.method == "POST":
        formulario = ComputadoraFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            tipo_computadora = data["tipo_computadora"]
            marca = data["marca"]
            modelo = data["modelo"]
            procesador = data["procesador"]
            ram = data["ram"]
            hhd = data["hhd"]
            computadora = Computadora(tipo_computadora=tipo_computadora, marca=marca, modelo=modelo, procesador=procesador, ram=ram, hhd=hhd)
            computadora.save()
            
            url_exitosa = reverse('computadoras') 
            return redirect(url_exitosa)
               
    else: # GET
        formulario = ComputadoraFormulario()
    http_response = render(
        request=request,
        template_name='catalogo/formulario_computadoras.html',
        context={'formulario' : formulario},
    )
    return http_response

########################################################################################################
#CREAR BUSCADORES

def buscar_cliente(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cliente = Cliente.objects.filter(apellido__icontains=busqueda)
        contexto = {
        "cliente": cliente,
        }
        
    http_response = render(
        request=request,
        template_name='catalogo/clientes.html',
        context=contexto,
    )
    return http_response

def buscar_computadora(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        computadora = Computadora.objects.filter(marca__icontains=busqueda)
        contexto = {
        "computadora": computadora,
        }
        
    http_response = render(
        request=request,
        template_name='catalogo/computadoras.html',
        context=contexto,
    )
    return http_response