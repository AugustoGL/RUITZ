from django.contrib import admin
from .models import Categoria
from .models import Color
from .models import Tamaño
from .models import Producto

admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Tamaño)
admin.site.register(Producto)
