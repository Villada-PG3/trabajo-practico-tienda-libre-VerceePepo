from django.shortcuts import render
from django.views.generic import TemplateView

class HolaTemplateView(TemplateView):
    template_name = 'hola.html'
