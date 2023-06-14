from django.urls import path
from .views import *


urlpatterns = [
    path('', adminMain, name = 'inicio'),

    path('productos/', products, name = 'productos'),
    path('productos/añadir_producto/', addProduct, name = 'añadir_productos'),
    path('productos/editar_producto/<int:codigo_de_barras>', editProducts, name = 'editar_producto'),
    path('productos/mostrar_productos/', showProducts, name = 'mostrar_productos'),
    path('productos/eliminar_producto/<int:codigo_de_barras>', deleteProduct, name = 'eliminar_producto'),

    path('proveedores/', providers, name = 'proveedores'),
    path('proveedores/mostrar_proveedores/', showProviders, name = 'mostrar_proveedores'),
    path('proveedores/editar_proveedor/<int:nit>', editProvider, name = 'editar_proveedor'),
    path('proveedores/eliminar_proveedor/<int:nit>', deleteProvider, name = 'eliminar_proveedor'),
    path('proveedores/añadir_proveedor/', addProviders, name = 'añadir_proveedores'),
]