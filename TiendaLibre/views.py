from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Producto



class HolaTemplateView(TemplateView):
    template_name = 'hola.html'

def productos(request):
    lista_productos = Producto.objects.all()

    context = {
        "productos": lista_productos
    }

    return render(request, "productos.html", context)


def home(request):
    productos_oferta = [
        {'nombre': 'Sanguche', 'precio': 120, 'stock': 6},
        {'nombre': 'Alfajor', 'precio': 200, 'stock': 12},
        {'nombre': 'Tatin', 'precio': 100, 'stock': 2},
        {'nombre': '67', 'precio': 67, 'stock': 67},
    ]
        
    
    context = {
        'Productos': productos_oferta,
        'usuario_logueado': True
    }
    return render(request, 'tiendalibre/home.html', context)

def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca_de_mi.html')
