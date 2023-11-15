from django.shortcuts import render
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
    busqueda = request.GET.get('buscador')
    productos, colores_seleccionados, categorias_seleccionadas, talles_seleccionados = filtrar_productos(request)
    if busqueda:
        productos = buscar(busqueda)
    return render(request, 'indumentaria.html', {
        'productos': productos,
        'colores': colores,
        'categorias': categorias,
        'talles': talles,
        'colores_seleccionados': colores_seleccionados,
        'categorias_seleccionadas': categorias_seleccionadas,
        'talles_seleccionados': talles_seleccionados,
    })






def Detalles(request, pk):
    producto = Producto.objects.all(id=pk)
    busqueda = request.GET.get('buscador')
    if busqueda:
        productos = buscar(busqueda)
        return render(request, "indumentaria.html", {'productos': productos})
    return render(request, "detalles.html", {'producto': producto})