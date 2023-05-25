from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ClienteForm, FacturaForm
from .models import Cliente, Factura


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


def venta(request):
    return render(request, 'cajero/no_client_purchase.html')


def cashier(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        if factura_form.is_valid():
            factura_form.save()
        
    else:
        factura_form = FacturaForm()
    
    return render(request, 'cajero/cashier.html', {'factura_form': factura_form})


def test(request):
    return render(request, 'cajero/not_found.html')