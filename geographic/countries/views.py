from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class Countries(TemplateView):
    template_name='countries/countries.html'
