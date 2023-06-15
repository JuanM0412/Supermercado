from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *


def inicioAdmin(request):
    return render(request, 'administrador/inicio_admin.html')


def proveedores(request):
    return render(request, 'administrador/proveedores/inicio_proveedor.html')


def añadirProveedor(request):
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
        
    else:
        proveedor_form = ProveedorForm()
    
    return render(request, 'administrador/proveedores/añadir.html', {'proveedor_form': proveedor_form})


def mostrarProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'administrador/proveedores/resultados.html', {'proveedores': proveedores})


def editarProveedor(request, nit):
    proveedor_form, error = None, None
    try:
        proveedor = Proveedor.objects.get(nit = nit)
        if request.method == 'GET':
            proveedor_form = ProveedorForm(instance = proveedor)
        else:
            proveedor_form = ProveedorForm(request.POST, instance = proveedor)
            if proveedor_form.is_valid():
                proveedor = proveedor_form.save(commit = False)
                proveedor.save()
                return redirect('proveedor:mostrar_proveedores')

    except ObjectDoesNotExist as e:
        error = f'No se ha encontrado un proveedor con el NIT {nit}.'

    return render(request, 'administrador/proveedores/modificar.html', {'proveedor_form': proveedor_form, 'error': error})


def eliminarProveedor(request, nit):
    proveedor = Proveedor.objects.get(nit = nit)
    proveedor.delete()
    return redirect('proveedor:mostrar_proveedores')


def productos(request):
    return render(request, 'administrador/productos/inicio_producto.html')


def añadirProducto(request):
    if request.method == 'POST':
        productos_form = ProductosForm(request.POST)
        if productos_form.is_valid():
            productos_form.save()
        
    else:
        productos_form = ProductosForm()
    
    return render(request, 'administrador/productos/añadir.html', {'productos_form': productos_form})


def mostrarProductos(request):
    productos = Productos.objects.all()
    return render(request, 'administrador/productos/resultados.html', {'productos': productos})


def editarProducto(request, codigo_de_barras):
    producto_form, error = None, None
    try:
        producto = Productos.objects.get(codigo_de_barras = codigo_de_barras)
        if request.method == 'GET':
            producto_form = ProductosForm(instance = producto)
        else:
            producto_form = ProductosForm(request.POST, instance = producto)
            if producto_form.is_valid():
                producto = producto_form.save(commit = False)
                producto.save()
                return redirect('proveedor:mostrar_productos')

    except ObjectDoesNotExist as e:
        error = f'No se ha encontrado un producto con el código de barras {codigo_de_barras}.'

    return render(request, 'administrador/productos/modificar.html', {'producto_form': producto_form, 'error': error})


def eliminarProducto(request, codigo_de_barras):
    producto = Productos.objects.get(codigo_de_barras = codigo_de_barras)
    producto.delete()
    return redirect('proveedor:mostrar_productos')