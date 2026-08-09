from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
]