from django.urls import path
from .views import manejarProveedores, Home, manejarProductos, mostrarProveedores, editarProveedor, mostrarProductos


urlpatterns = [
    path('añadir_proveedores/', manejarProveedores, name = 'añadir_proveedores'),
    path('home/', Home, name = 'home'),
    path('añadir_productos/', manejarProductos, name = 'añadir_productos'),
    path('mostrar_proveedores/', mostrarProveedores, name = 'mostrar_proveedores'),
    path('editar_proveedor/<int:nit>', editarProveedor, name = 'editar_proveedores'),
    path('mostrar_productos/', mostrarProductos, name = 'mostrar_productos'),
]