from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Producto, Categoria
from django.shortcuts import get_object_or_404



class HolaTemplateView(TemplateView):
    template_name = 'hola.html'




def home(request):
    productos = Producto.objects.filter(disponible=True).order_by('fecha_creacion')[:3] 
        
    
    context = {
        'Productos': productos,
        'usuario_logueado': True
    }
    return render(request, 'tiendalibre/home.html', context)

def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca_de_mi.html')

def catalogo(request):
    productos = Producto.objects.filter(disponible=True).order_by('stock')
    context = {
        'productos': productos
    }
    return render(request, 'tiendalibre/catalogo.html', context)

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {
        'producto': producto
    }
    return render(request, 'tiendalibre/detalle.html', context)
