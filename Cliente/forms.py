from django import forms
from .models import Servicio


class FormServicio(forms.ModelForm):    
    class Meta:
        model = Servicio
        exclude = ['codigo','estado']

class FormCodigo(forms.ModelForm):    
    class Meta:
        model = Servicio
        fields = ['codigo']




