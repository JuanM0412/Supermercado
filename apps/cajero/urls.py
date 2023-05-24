from django.urls import path
from .views import manejarClientes, mostrarClientes, editarCliente

urlpatterns = [
    path('clientes/manejar_clientes/', manejarClientes, name = 'manejar_clientes'),
    path('clientes/mostrar_clientes/', mostrarClientes, name = 'mostrar_clientes'),
    path('clientes/editar_cliente/<int:cedula>', editarCliente, name = 'editar_cliente'),
]