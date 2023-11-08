from django.shortcuts import render
from django.views import View
from .forms import FormCodigo
from .models import Cliente

class CodigoForm(View):
    def get(self,request,*args, **kwargs):
        contexto = {
            'formulario':FormCodigo()
        }
        return render(request,'home.html',contexto)
    
    def post(self,request,*args, **kwargs):
        form = FormCodigo(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data.get('codigo')
            print(codigo)
            try:
                cliente = Cliente.objects.get(codigo=codigo)
            except Cliente.DoesNotExist:
                form.add_error('codigo', 'Código no encontrado, por favor vuelve a intentarlo.')
                return render(request, 'home.html', {'formulario': form})
            contexto = {
                "cliente":cliente.get_data()
            }
            return render(request,"pedido.html",contexto)        
        return render(request,'home.html', {'formulario': form})