from django import forms
from .models import Venta, Cliente, Factura


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
        fields = ['fecha', 'cliente_cedula']