from TiendaLibre.models import Producto, Categoria

Producto.objects.all()

Producto.objects.count()

Producto.objects.first()

Producto.objects.filter(precio__gt=10000)

Producto.objects.filter(precio__lte=50000)

Producto.objects.filter(nombre__icontains="Aquarius")

Categoria.objects.all()

Categoria.objects.filter(nombre__icontains="Gaseosa")

Producto.objects.filter(
    precio__gte=10000,
    precio__lte=50000
)

Producto.objects.all().order_by("precio")