from django.shortcuts import render
from django.http import HttpResponse #Se importa el objeto HttpResponse para poder retornar la vista.
# Create your views here.

def home(request):
    return HttpResponse('Página principal')

def continents(request):
    return HttpResponse('Continentes del mundo')
