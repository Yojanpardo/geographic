from django.shortcuts import render
from django.http import HttpResponse #Se importa el objeto HttpResponse para poder retornar la vista.
# Create your views here.

def home(request):
    return render(request, 'continents/home.html')

def continents(request):
    return render(request, 'continents/continents.html')
