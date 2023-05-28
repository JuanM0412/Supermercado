from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import Cliente, Factura, Venta
from apps.administrador.models import Productos


def manejarClientes(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
        
    else:
        cliente_form = ClienteForm()
    
    return render(request, 'cajero/cliente/add.html', {'cliente_form': cliente_form})


def mostrarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cajero/cliente/results.html', {'clientes': clientes})


def editarCliente(request, cedula):
    cliente_form, error = None, None
    try:
        cliente = Cliente.objects.get(cedula = cedula)
        if request.method == 'GET':
            cliente_form = ClienteForm(instance = cliente)
        else:
            cliente_form = ClienteForm(request.POST, instance = cliente)
            if cliente_form.is_valid():
                cliente = cliente_form.save(commit = False)
                cliente.save()
                return redirect('cajero:mostrar_clientes')

    except ObjectDoesNotExist as e:
        error = f'No se ha encontrado un cliente con la cédula {cedula}.'

    return render(request, 'cajero/cliente/modify.html', {'cliente_form': cliente_form, 'error': error})


def eliminarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula = cedula)
    cliente.delete()
    return redirect('cajero:mostrar_clientes')


def registrarFactura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        if factura_form.is_valid():
            factura_form.save()
            id = Factura.id
            return redirect('cajero:manejar_venta', id)
        
    else:
        factura_form = FacturaForm()
    
    return render(request, 'cajero/cashier.html', {'factura_form': factura_form})


from .models import Factura

def manejarVentas(request, id_factura):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save(commit = False)
            factura = Factura.objects.get(pk = id_factura)
            venta.id_factura = factura 
            venta.save()

    else:
        venta_form = VentaForm()
    
    return render(request, 'cajero/purchase.html', {'venta_form': venta_form})


def resumenVenta(request, id_factura):
    venta = Venta.objects.get(id_factura=id_factura)
    factura = venta.id_factura
    cliente = factura.cliente_cedula
    productos = venta.productos_codigo_de_barras
    return render(request, 'cajero/not_found.html', {'venta': venta, 'factura': factura, 'cliente': cliente, 'productos': productos})


def test(request):
    return render(request, 'cajero/not_found.html')