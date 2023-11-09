from django import forms

class BusquedaProductosForm(forms.Form):
    termino_busqueda = forms.CharField(required=False, label='Buscar productos')


