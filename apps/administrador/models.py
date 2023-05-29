from django.db import models


class Proveedor(models.Model):
    nit = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 60, blank = False, null = False)
    direccion = models.CharField(max_length = 60, blank = False, null = False)
    telefono = models.CharField(max_length = 20, blank = False, null = False)
    productos = models.TextField(blank = False, null = False)

    class Meta:
        db_table = 'proveedor'
        ordering = ['nit']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Productos(models.Model):
    codigo_de_barras = models.IntegerField(primary_key = True)
    stock = models.IntegerField(blank = False, null = False)
    precio_compra = models.IntegerField(blank = False, null = False)
    precio_venta = models.IntegerField(blank = False, null = False)
    nombre = models.CharField(blank = False, null = False, max_length = 60)
    unidades_vendidas = models.IntegerField(blank = False, null = False)
    ganancia = models.IntegerField(blank = False, null = False)
    proveedor_nit = models.IntegerField(blank = False, null = False)

    class Meta:
        db_table = 'productos'
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'