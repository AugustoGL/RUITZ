from django.shortcuts import render, redirect
from .models import Producto
from django.db.models import Q
from .models import *

def Home(request):
    talles = Tamaño.objects.all()
    colores = Color.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    busqueda = request.GET.get('buscador')
    if busqueda:
        productos_relacionados = productos.filter(
            Q(nombre__icontains=busqueda) |
            Q(categoria__nombre__icontains=busqueda) |
            Q(colores__nombre__icontains=busqueda)).distinct()
        productos_no_relacionados = productos.exclude(id__in=productos_relacionados.values_list('id', flat=True))
        productos = list(productos_relacionados) + list(productos_no_relacionados)
        return render(request, "indumentaria.html", {'productos': productos, 'talles': talles, 'colores': colores, 'categorias': categorias})
    return render(request, "home.html", {'productos': productos, 'talles': talles, 'colores': colores, 'categorias': categorias})

def Indumentaria(request):
    talles = Tamaño.objects.all()
    colores = Color.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    busqueda = request.GET.get('buscador')
    if busqueda:
        productos_relacionados = productos.filter(
            Q(nombre__icontains=busqueda) |
            Q(categoria__nombre__icontains=busqueda) |
            Q(colores__nombre__icontains=busqueda)).distinct()
        productos_no_relacionados = productos.exclude(id__in=productos_relacionados.values_list('id', flat=True))
        productos = list(productos_relacionados) + list(productos_no_relacionados)

    return render(request, "indumentaria.html", {'productos': productos, 'talles': talles, 'colores': colores, 'categorias': categorias})
