from django.db import models

# Modelo para Categorías de Productos
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Tamaños
class Tamaño(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

# Modelo para Productos
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tamaño = models.ForeignKey(Tamaño, on_delete=models.SET_NULL, null=True, blank=True) # Un producto puede tener un solo tamaño
    editable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
