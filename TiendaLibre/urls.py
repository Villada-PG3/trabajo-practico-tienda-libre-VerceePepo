from django.urls import path
from . import views
from .views import HomeView, CatalogoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('catalogo', CatalogoView.as_view(), name='catalogo'),
    path('detalle/<int:pk>/', views.DetalleView.as_view(), name='detalle'),
]