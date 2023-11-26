from django.db.models import Q
from .models import *
from django.shortcuts import render


def buscar(busqueda):
    print(busqueda)
    productos = Producto.objects.all()
    productos_relacionados = productos.filter(
        Q(nombre__icontains=busqueda) |
        Q(categoria__nombre__icontains=busqueda) |
        Q(colores__nombre__icontains=busqueda)).distinct()
    print(productos_relacionados)
    productos_no_relacionados = productos.exclude(id__in=productos_relacionados.values_list('id', flat=True))
    resultado = list(productos_relacionados) + list(productos_no_relacionados)
    return resultado

def filtrar_productos(request):
    cos = request.GET.getlist('colores')
    cas = request.GET.getlist('categorias')
    tas = request.GET.getlist('talles')
    condiciones_filtrado = Q()
    if cos:
        condiciones_filtrado &= Q(colores__id__in=cos)
    if cas:
        condiciones_filtrado &= Q(categoria__id__in=cas)
    if tas:
        condiciones_filtrado &= Q(tamaño__id__in=tas)

    productos = Producto.objects.filter(condiciones_filtrado).distinct()
    respuesta = [productos, cos, cas, tas]
    return respuesta