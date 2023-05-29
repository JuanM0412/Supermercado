from django.db import models
from datetime import datetime
from apps.administrador.models import Productos


class Cliente(models.Model):
    cedula = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 60, blank = True, null = True)
    direccion = models.CharField(max_length = 60, blank = True, null = True)
    telefono = models.CharField(max_length = 20, blank = True, null = True)

    class Meta:
        db_table = 'cliente'
        ordering = ['nombre']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Factura(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.CharField(max_length = 20, blank = False, null = False)
    cliente_cedula = models.IntegerField(blank = False, null = False)

    class Meta:
        db_table = 'factura'
        ordering = ['id']
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


class Venta(models.Model):
    id = models.AutoField(primary_key = True)
    id_factura = models.IntegerField(blank = False, null = False)
    productos_codigo_de_barras = models.IntegerField(blank = False, null = False)
    cantidad = models.IntegerField(blank = False, null = False)
    valor_producto_comprado = models.IntegerField(blank = False, null = False)

    class Meta:
        db_table = 'venta'
        ordering = ['id_factura']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'