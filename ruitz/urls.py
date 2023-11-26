from django.urls import path
from . views import * 

urlpatterns = [
path('', HomeView.as_view(), name='home'),
path('indumentaria/', IndumentariaView.as_view(), name='indumentaria'),
path('articulo/<int:pk>/', ArticuloView.as_view(), name='articulo'),
]