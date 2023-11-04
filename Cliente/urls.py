
app_name = 'clientes'

from django.urls import path
from .views import Patron, CodigoForm

urlpatterns = [
    path('',Patron,name='home'),
    path('fcodigo/',CodigoForm.as_view(),name='formCodigo'),
]

