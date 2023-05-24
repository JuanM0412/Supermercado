from django.contrib import admin
from .models import Proveedor, Productos, Venta, Cliente, Factura

admin.site.register(Proveedor)
admin.site.register(Productos)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Venta)