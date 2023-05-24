from django.urls import path
from .views import manejarProveedores, Home, manejarProductos, mostrarProveedores, editarProveedor, mostrarProductos, proveedores, productos, buscarProveedor, buscarProducto


urlpatterns = [
    path('home/', Home, name = 'home'),
    path('proveedores/añadir_proveedores/', manejarProveedores, name = 'añadir_proveedores'),
    path('productos/añadir_productos/', manejarProductos, name = 'añadir_productos'),
    path('proveedores/mostrar_proveedores/', mostrarProveedores, name = 'mostrar_proveedores'),
    path('proveedores/editar_proveedor/<int:nit>', editarProveedor, name = 'editar_proveedores'),
    path('productos/mostrar_productos/', mostrarProductos, name = 'mostrar_productos'),
    path('proveedor/buscar_proveedor/', buscarProveedor, name = 'buscar_proveedor'),
    path('producto/buscar_producto/', buscarProducto, name = 'buscar_producto'),
    path('proveedores/', proveedores, name = 'proveedores'),
    path('productos/', productos, name = 'productos'),
]