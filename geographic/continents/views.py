from django.shortcuts import render
from django.http import HttpResponse #Se importa el objeto HttpResponse para poder retornar la vista.
from django.views.generic import View
# Create your views here.

def home(request):
    return render(request, 'continents/home.html')

class Continents(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'continents/continents.html')
