from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q

class VistaBase(View):

    def __init__(self):
        super().__init__()
        self.productos = Producto.objects.all()
        self.talles = Tamaño.objects.all()
        self.colores = Color.objects.all()
        self.categorias = Categoria.objects.all()
        self.template_name = "Home.html"  # Definir esto en las subclases


    def buscar(self, request):
        if request.method == 'GET':
            busqueda = request.GET.get('buscador')
            if busqueda:
                productos_relacionados = self.productos.filter(
                    Q(nombre__icontains=busqueda) |
                    Q(categoria__nombre__icontains=busqueda) |
                    Q(colores__nombre__icontains=busqueda)
                ).distinct()
                productos_no_relacionados = self.productos.exclude(id__in=productos_relacionados.values_list('id', flat=True))
                self.productos = list(productos_relacionados) + list(productos_no_relacionados)
                self.template_name = 'indumentaria.html'
                return self.productos
        return self.productos

    def get_context_data(self):
        context = {
            'productos': self.productos,
            'talles': self.talles,
            'colores': self.colores,
            'categorias': self.categorias,
        }
        return context

    def render(self, context=None):
        return render(self.request, self.template_name, context)


class HomeView(VistaBase):

    def get(self, request):
        self.buscar(request)
        context = self.get_context_data()
        return self.render(context)


class IndumentariaView(VistaBase):

    def filtrar(self, request):
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

        self.productos = Producto.objects.filter(condiciones_filtrado).distinct()

        print(self.productos)

    def get(self, request):
        self.buscar(request)
        if 'filtrar' in request.GET:
            self.filtrar(request)   
        self.template_name = 'indumentaria.html'
        context = self.get_context_data()
        context.update({
            'colores_seleccionados': request.GET.getlist('colores'),
            'categorias_seleccionadas': request.GET.getlist('categorias'),
            'talles_seleccionados': request.GET.getlist('talles'),
        })
        return self.render(context)


class ArticuloView(VistaBase):
    

    def get(self, request, pk):
        self.buscar(request)
        self.template_name = 'articulo.html'
        producto = get_object_or_404(Producto, pk=pk)
        context = self.get_context_data()
        context.update({
            'producto': producto,
        })
        return self.render(context)