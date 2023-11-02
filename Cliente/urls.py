
app_name = 'clientes'

from django.urls import path
from .views import Patron, ClienteForm, CodigoForm

urlpatterns = [
    path('',Patron,name='home'),
    path('fcliente/',ClienteForm.as_view(),name='formCliente'),
    path('fcodigo/',CodigoForm.as_view(),name='formCodigo'),
]

