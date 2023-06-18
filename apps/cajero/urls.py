from django.urls import path
from .views import *

urlpatterns = [
    path('', inicioCajero, name = 'inicio_cajero'),

    path('clientes/', inicioClientes, name = 'clientes'),
    path('clientes/añadir_cliente/', añadirClientes, name = 'añadir_cliente'),
    path('clientes/mostrar_clientes/', mostrarClientes, name = 'mostrar_clientes'),
    path('clientes/editar_cliente/<int:cedula>', editarCliente, name = 'editar_cliente'),
    path('clientes/eliminar_cliente/<int:cedula>', eliminarCliente, name = 'eliminar_cliente'),

    path('venta/registrar_venta/<int:id_factura>', registrarVenta, name = 'registrar_venta'),
    path('venta/resumen/<int:id_factura>', resumenVenta, name = 'resumen'),
    path('venta/factura/', registrarFactura, name = 'factura'),
    path('venta/historico/<int:cedula>', historicoVentas, name = 'historico'),
]