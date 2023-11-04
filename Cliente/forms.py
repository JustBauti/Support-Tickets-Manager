from django import forms
from .models import Cliente


class FormCliente(forms.ModelForm):    
    class Meta:
        model = Cliente
        exclude = ['codigo','estado']

class FormCodigo(forms.ModelForm):    
    class Meta:
        model = Cliente
        fields = ['codigo']




