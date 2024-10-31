from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from .models import Colores
from .forms import BuscarEsmalteFormulario, CearEsmalteFormulario


# Create your views here.
def inicio(request):
    return render (request, 'index.html')


def listado_colores(request):
    return HttpResponse('Listado de colores: ')

def buscar_esmalte(request):
    if request.method == 'POST':
        formulario = BuscarEsmalteFormulario(request.POST)
        
        if formulario.is_valid():
            color = formulario.cleaned_data('color')
            marca = formulario.cleaned_data('marca')
            esmaltes = Colores(color=color, marca=marca)
            esmaltes.save()
    return render (request, 'buscar_esmalte.html', {'form':'formulario'})


def primer_template(request):
    with open(r'templates\primer_template.html') as archivo_del_template:
        template = Template(archivo_del_template.read())

    contexto = Context()  
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)


def segundo_template(request):
    
    fecha_actual = datetime.now()
    datos = {'fecha_actual': fecha_actual,
             'numeros': list(range(1, 11))}
    
    return render(request, 'segundo_template.html', datos)

def crear_esmaltes(request):
    
    print('Request', request) 
    print('GET', request.GET)
    print('POST', request.POST)
    
    formulario = CearEsmalteFormulario()
    
    if request.method == 'POST':
        formulario = CearEsmalteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            colores = Colores(marca=data.get('marca'), color=data.get('color'))
            colores.save() 
            
    return render(request, 'crear_color_esmalte.html', {'form': formulario})






   

