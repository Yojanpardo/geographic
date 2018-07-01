from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class People(TemplateView):
    template_name = 'people/people.html'
