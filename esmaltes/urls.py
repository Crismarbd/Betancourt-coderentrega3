from django.urls import path
from .views import inicio, buscar_esmaltes, crear_esmaltes, mi_vista

urlpatterns = [
     path('', inicio, name='inicio'),
     path('buscar-esmalte/', buscar_esmaltes, name='buscar_esmaltes'),
     path('crear-esmaltes/', crear_esmaltes, name='crear_esmaltes'),
     path('mi-vista/', mi_vista, name='mi_vista')
    
    
]
