from django.contrib import admin
from .models import Categoria
from .models import Color
from .models import Tamaño
from .models import Producto
from django.contrib import admin
from django.contrib.sites.models import Site

admin.site.unregister(Site)  # Desregistrar la configuración de sitio predeterminada
admin.site.site_url = 'https://tallerismo.com.ar'  # Configurar la URL del sitio correctamente

admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Tamaño)
admin.site.register(Producto)
