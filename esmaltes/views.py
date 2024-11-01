from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from .models import Colores
from .forms import BuscarEsmalteFormulario, CearEsmalteFormulario


# Create your views here.
def inicio(request):
    return render (request, 'index.html')

def buscar_esmaltes(request):
    
    formulario=BuscarEsmalteFormulario(request.GET)
    esmaltes=Colores.objects.all()
    if formulario.is_valid():
        marca=formulario.cleaned_data.get('marca')
        if marca:
            esmaltes=Colores.objects.filter(marca__icontains=marca)
        
    return render (request, 'buscar_esmalte.html', {'esmaltes': esmaltes, 'forms': formulario})

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

def mi_vista(request):
    return render(request, 'mi_vista.html')






   

