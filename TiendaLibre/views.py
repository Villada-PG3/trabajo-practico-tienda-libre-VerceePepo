from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Producto



class HolaTemplateView(TemplateView):
    template_name = 'hola.html'

def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "productos.html", contexto)


def home(request):
    return render(request, 'tiendalibre/home.html')

def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca_de_mi.html')
