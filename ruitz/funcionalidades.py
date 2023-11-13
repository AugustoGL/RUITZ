from django.db.models import Q
from .models import *



def buscar(busqueda):
    productos = Producto.objects.all()
    productos_relacionados = productos.filter(
        Q(nombre__icontains=busqueda) |
        Q(categoria__nombre__icontains=busqueda) |
        Q(colores__nombre__icontains=busqueda)).distinct()
    productos_no_relacionados = productos.exclude(id__in=productos_relacionados.values_list('id', flat=True))
    resultado = list(productos_relacionados) + list(productos_no_relacionados)
    return resultado