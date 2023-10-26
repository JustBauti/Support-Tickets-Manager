from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import FormCliente, FormCodigo
from .models import Cliente
from django.views.generic import View
from secrets import choice


def HelloWorld(request):
    return render(request,'home.html',{})

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
            formulario = FormCodigo(request.POST)
            
            if formulario.is_valid() and Cliente.objects.filter(codigo = request.POST['codigo']) != '':
                print(Cliente.objects.filter(codigo = request.POST['codigo'])[0].data())
                contexto = {
                    "cliente":Cliente.objects.filter(codigo = request.POST['codigo'])[0].data(),
                    "1":'En produccion',
                    "2":'Listo para retirar',
                    "0":'Aceptado'
                }
                return render(request,"pedido.html",contexto)
            
            return render(request,'formCodigo.html', {})
        
        return render(request,'formCodigo.html', {})

