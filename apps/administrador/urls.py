from django.urls import path
from .views import *


urlpatterns = [
    path('home/', Home, name = 'home'),

    path('productos/', productos, name = 'productos'),
    path('productos/añadir_productos/', manejarProductos, name = 'añadir_productos'),
    path('productos/buscar_producto/', buscarProducto, name = 'buscar_producto'),
    path('productos/editar_productos/<int:codigo_de_barras>', editarProductos, name = 'editar_productos'),
    path('productos/mostrar_productos/', mostrarProductos, name = 'mostrar_productos'),
    path('productos/eliminar_producto/<int:codigo_de_barras>', eliminarProducto, name = 'eliminar_producto'),

    path('proveedores/', proveedores, name = 'proveedores'),
    path('proveedores/mostrar_proveedores/', mostrarProveedores, name = 'mostrar_proveedores'),
    path('proveedores/editar_proveedor/<int:nit>', editarProveedor, name = 'editar_proveedores'),
    path('proveedores/eliminar_proveedor/<int:nit>', eliminarProveedor, name = 'eliminar_proveedor'),
    path('proveedores/añadir_proveedores/', manejarProveedores, name = 'añadir_proveedores'),
    path('proveedor/buscar_proveedor/', buscarProveedor, name = 'buscar_proveedor'),
]