from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import ClienteForm
from .models import Cliente


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
                cliente_form.save()

    except ObjectDoesNotExist as e:
        error = f'No se ha encontrado un cliente con la cédula {cedula}.'

    return render(request, 'cajero/cliente/modify.html', {'cliente_form': cliente_form, 'error': error})
