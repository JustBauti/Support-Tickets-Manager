from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import FormCliente, FormCodigo
from .models import Cliente
from django.views.generic import View
from secrets import choice


def Patron(request):
    return render(request,'index.html',{})

class ClienteForm(View):
    def get(self,request,*args, **kwargs):
        contexto = {
            'formulario':FormCliente()
        }
        return render(request,'formCliente.html',contexto)
    
    def codigoGenerator(self):
        c = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join([choice(c) for i in range(50)])

    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            formulario = FormCliente(request.POST)
            if formulario.is_valid():
                cliente = formulario.save(commit=False)
                cliente.codigo = self.codigoGenerator()
                cliente.save()
                return redirect('clientes:home')
        return render(request,'formCliente.html', {})


class CodigoForm(View):
    def get(self,request,*args, **kwargs):
        contexto = {
            'formulario':FormCodigo()
        }
        return render(request,'formCodigo.html',contexto)
    
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            c = get_object_or_404(Cliente, codigo=request.POST['codigo']).data()
                       
            if FormCodigo(request.POST).is_valid():
                contexto = {
                    "nombre":c['nombres'],
                    "estado":c["estado"],
                    "problema":c['problema'],
                    "1":'En produccion',
                    "2":'Listo para retirar',
                    "0":'Aceptado'
                }
                return render(request,"pedido.html",contexto)        
        return render(request,'formCodigo.html', {})

