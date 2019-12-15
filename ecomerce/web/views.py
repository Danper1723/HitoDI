from django.shortcuts import render
from web.models import Tienda

def tienda_index(request):
    tienda = Tienda.objects.all()
    context = {
        'tienda': tienda
    }
    return render(request, 'tienda_index.html', context)

def tienda_detalle(request, pk):
    i = Tienda.objects.get(pk=pk)
    context = {
        'i': i
    }
    return render(request, 'tienda_detalle.html', context)