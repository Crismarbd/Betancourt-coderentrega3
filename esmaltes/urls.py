from django.urls import path
from .views import inicio, listado_colores, buscar_esmalte, primer_template, segundo_template, crear_esmaltes

urlpatterns = [
     path('', inicio, name='inicio'),
     path('listado-colores/', listado_colores, name='listado_colores'),
     path('buscar-esmalte/', buscar_esmalte, name='buscar_esmalte'),
     path('primer-template/', primer_template, name='primer_template'),
     path('segundo-template/', segundo_template, name='segundo_template'),
     path('crear-esmaltes/', crear_esmaltes, name='crear_esmaltes')
    
    
]
