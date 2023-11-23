
app_name = 'servicios'

from django.urls import path
from .views import CodigoForm

urlpatterns = [
    path('',CodigoForm.as_view(),name='formCodigo'),
]

