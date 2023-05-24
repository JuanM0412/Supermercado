from django.urls import path
from .views import manejarClientes

urlpatterns = [
    path('clientes/manejar_clientes/', manejarClientes, name = 'manejar_clientes'),
]