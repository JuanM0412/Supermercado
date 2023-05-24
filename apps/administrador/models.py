from django.db import models
from datetime import datetime

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
    proveedor_nit = models.ForeignKey(Proveedor, on_delete = models.CASCADE, related_name = 'a')

    class Meta:
        db_table = 'productos'
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


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
    fecha = models.DateTimeField(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    cliente_cedula = models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name = 'b')

    class Meta:
        db_table = 'factura'
        ordering = ['id']
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


class Venta(models.Model):
    id = models.AutoField(primary_key = True)
    id_factura = models.ForeignKey(Factura, on_delete = models.CASCADE, related_name = 'c')
    productos_codigo_de_barras = models.ForeignKey(Productos, on_delete = models.CASCADE, related_name = 'd')
    cantidad = models.IntegerField(blank = False, null = False)
    valor_producto_comprado = models.IntegerField(blank = False, null = False)

    class Meta:
        db_table = 'venta'
        ordering = ['id_factura']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'