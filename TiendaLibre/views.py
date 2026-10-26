from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q



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
    paginate_by = 8
    
    def get_queryset(self):
        busqueda = self.request.GET.get('q')

        queryset = Producto.objects.filter(
            disponible=True
        ).order_by('stock')

        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(marca__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )

        return queryset
    



class DetalleView(DetailView):
    model = Producto
    template_name = 'tiendalibre/detalle.html'
    context_object_name = 'producto'
    
    
    
class CategoriaView(ListView):
    model = Producto
    template_name = 'tiendalibre/categoria.html'
    context_object_name = 'productos'
    paginate_by = 8

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        categoria = get_object_or_404(Categoria, slug=slug)
        return Producto.objects.filter(categoria=categoria, disponible=True).order_by('stock')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        categoria = get_object_or_404(Categoria, slug=slug)
        context['categoria'] = categoria
        return context
    
    

