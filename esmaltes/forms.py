from django import forms
from .models import Colores

class CearEsmalteFormulario(forms.Form):
    color = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)

class BuscarEsmalteFormulario(forms.Form):
    
    marca = forms.CharField(max_length=20)