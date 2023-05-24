from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProveedorForm, ProductosForm
from .models import Proveedor, Productos


def proveedores(request):
    return render(request, 'administrador/proveedores/supplier.html')


def productos(request):
    return render(request, 'administrador/productos/product.html')


def manejarProveedores(request):
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
        
    else:
        proveedor_form = ProveedorForm()
    
    return render(request, 'administrador/proveedores/add.html', {'proveedor_form': proveedor_form})


def manejarProductos(request):
    if request.method == 'POST':
        productos_form = ProductosForm(request.POST)
        if productos_form.is_valid():
            productos_form.save()
        
    else:
        productos_form = ProductosForm()
    
    return render(request, 'administrador/productos/add.html', {'productos_form': productos_form})


def mostrarProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'administrador/proveedores/results.html', {'proveedores': proveedores})


def mostrarProductos(request):
    productos = Productos.objects.all()
    return render(request, 'administrador/productos/results.html', {'productos': productos})


def editarProveedor(request, nit):
    proveedor_form, error = None, None
    try:
        proveedor = Proveedor.objects.get(nit = nit)
        if request.method == 'GET':
            proveedor_form = ProveedorForm(instance = proveedor)
        else:
            proveedor_form = ProveedorForm(request.POST, instance = proveedor)
            if proveedor_form.is_valid():
                proveedor_form.save()

    except ObjectDoesNotExist as e:
        error = f'No se ha encontrado un proveedor con el NIT {nit}.'

    return render(request, 'administrador/proveedores/modify.html', {'proveedor_form': proveedor_form, 'error': error})


def buscarProveedor(request):
    return render(request, 'administrador/proveedores/search.html')


def buscarProducto(request):
    return render(request, 'administrador/productos/search.html')


def Home(request):
    return render(request, 'home.html')