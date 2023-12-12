from django.shortcuts import render
from django.views import View
from .forms import FormCodigo
from .models import Servicio

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
            try:
                servicio = Servicio.objects.get(codigo=codigo)
            except Servicio.DoesNotExist:
                form.add_error('codigo', 'Código no encontrado, por favor vuelve a intentarlo.')
                return render(request, 'home.html', {'formulario': form})
            contexto = {
                "servicio":servicio.get_data()
            }
            return render(request,"pedido.html",contexto)        
        return render(request,'home.html', {'formulario': form})