from django.shortcuts import get_object_or_404, redirect, render
from .forms import FormCodigo
from .models import Cliente
from django.views.generic import View


def Patron(request):
    return render(request,'patron.html',{})

class CodigoForm(View):
    def get(self,request,*args, **kwargs):
        contexto = {
            'formulario':FormCodigo()
        }
        return render(request,'codigo.html',contexto)
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            c = get_object_or_404(Cliente, codigo=request.POST['codigo']).get_data()
                       
            if FormCodigo(request.POST).is_valid():
                contexto = {
                    "cliente":c
                }
                return render(request,"pedido.html",contexto)        
        return render(request,'form_codigo.html', {})

