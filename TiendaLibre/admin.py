from django.contrib import admin
from .models import Categoria, Producto
from django.utils.html import format_html



admin.site.register(Categoria)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'stock', 'fecha_creacion', 'mostrar_imagen')
    
    readonly_fields = ('imagen_detalle',)
    
    def mostrar_imagen(self, obj):
        if obj.imagen:
             return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.imagen.url)
        return "Sin imagen"
    
    mostrar_imagen.short_description = 'Imagen'
        
    def imagen_detalle(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 200px; height: 200px; object-fit: cover; border-radius: 4px;" />', obj.imagen.url)
        return "Sin imagen"
    
    imagen_detalle.short_description = 'Imagen'
