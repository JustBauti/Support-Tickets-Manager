
app_name = 'clientes'

from django.urls import path
from .views import CodigoForm

urlpatterns = [
    path('',CodigoForm.as_view(),name='formCodigo'),
]

