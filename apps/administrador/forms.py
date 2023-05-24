from django import forms
from .models import Proveedor, Productos, Venta, Cliente, Factura


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nit', 'nombre', 'direccion', 'telefono', 'productos']


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['codigo_de_barras', 'stock', 'precio_compra', 'precio_venta', 'nombre', 'unidades_vendidas', 'ganancia', 'proveedor_nit']


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['id', 'id_factura', 'productos_codigo_de_barras', 'cantidad', 'valor_producto_comprado']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'direccion', 'telefono']


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['id', 'fecha', 'cliente_cedula']