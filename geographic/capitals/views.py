from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Capitals(TemplateView):
    template_name = 'capitals/capitals.html'
