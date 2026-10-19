from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto, Categoria
from django.shortcuts import get_object_or_404



class HolaTemplateView(TemplateView):
    template_name = 'hola.html'


class HomeView(TemplateView):
    template_name = 'tiendalibre/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        productos = Producto.objects.filter(disponible=True).order_by('-fecha_creacion')[:3]
        context['Productos'] = productos
        context['usuario_logueado'] = True
        return context



def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca_de_mi.html')



class CatalogoView(ListView):
    model = Producto
    template_name = 'tiendalibre/catalogo.html'
    context_object_name = 'productos'
    queryset = Producto.objects.filter(disponible=True).order_by('stock')
    paginate_by = 8
    



class DetalleView(DetailView):
    model = Producto
    template_name = 'tiendalibre/detalle.html'
    context_object_name = 'producto'
    
