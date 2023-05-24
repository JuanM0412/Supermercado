from django.shortcuts import render
from .forms import ClienteForm


def manejarClientes(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
        
    else:
        cliente_form = ClienteForm()
    
    return render(request, 'cajero/cliente/add.html', {'cliente_form': cliente_form})