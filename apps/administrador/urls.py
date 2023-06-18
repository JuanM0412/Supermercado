from django.urls import path
from .views import *


urlpatterns = [
    path('', inicioAdministrador, name = 'inicio'),

    path('productos/', inicioProductos, name = 'productos'),
    path('productos/añadir_producto/', añadirProducto, name = 'añadir_productos'),
    path('productos/editar_producto/<int:codigo_de_barras>', editarProducto, name = 'editar_producto'),
    path('productos/mostrar_productos/', mostrarProductos, name = 'mostrar_productos'),
    path('productos/eliminar_producto/<int:codigo_de_barras>', eliminarProducto, name = 'eliminar_producto'),

    path('proveedores/', inicioProveedores, name = 'proveedores'),
    path('proveedores/mostrar_proveedores/', mostrarProveedores, name = 'mostrar_proveedores'),
    path('proveedores/editar_proveedor/<int:nit>', editarProveedor, name = 'editar_proveedor'),
    path('proveedores/eliminar_proveedor/<int:nit>', eliminarProveedor, name = 'eliminar_proveedor'),
    path('proveedores/añadir_proveedor/', añadirProveedor, name = 'añadir_proveedores'),
]