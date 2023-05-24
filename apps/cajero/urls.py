from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/manejar_clientes/', manejarClientes, name = 'manejar_clientes'),
    path('clientes/mostrar_clientes/', mostrarClientes, name = 'mostrar_clientes'),
    path('clientes/editar_cliente/<int:cedula>', editarCliente, name = 'editar_cliente'),
    path('clientes/eliminar_cliente/<int:cedula>', eliminarCliente, name = 'eliminar_cliente'),
    path('venta/', venta, name = 'venta'),
    path('cashier/', cashier, name = 'cashier'),
    path('test/', test, name = 'test'),
]