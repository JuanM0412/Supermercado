from django import forms
from .models import Proveedor, Productos


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nit', 'nombre', 'direccion', 'telefono', 'productos']


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['codigo_de_barras', 'stock', 'precio_compra', 'precio_venta', 'nombre', 'unidades_vendidas', 'ganancia', 'proveedor_nit']