from django.contrib import admin
from .models import Venta, Cliente, Factura


admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Venta)