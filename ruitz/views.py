from django.shortcuts import render, redirect
from .models import Producto
from .models import *
from .funcionalidades import *


def Home(request):
    talles = Tamaño.objects.all()
    colores = Color.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    busqueda = request.GET.get('buscador')
    if busqueda:
        productos = buscar(busqueda)
        return render(request, "indumentaria.html", {'productos': productos, 'talles': talles, 'colores': colores, 'categorias': categorias})
    return render(request, "home.html", {'productos': productos, 'talles': talles, 'colores': colores, 'categorias': categorias})

def Indumentaria(request):
    talles = Tamaño.objects.all()
    colores = Color.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    busqueda = request.GET.get('buscador')
    if busqueda:
        productos = buscar(busqueda)
    return render(request, "indumentaria.html", {'productos': productos, 'talles': talles, 'colores': colores, 'categorias': categorias})
