from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 #Se importa el objeto HttpResponse para poder retornar la vista.
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Continent
from django.views.generic.detail import DetailView
from .forms import RegisterContinentForm

# Create your views here.

def home(request):
    return render(request, 'continents/home.html')

class Continents(ListView):
    model = Continent
    template_name='continents/continents.html'

class ContinentDetailView(DetailView):
    template_name = 'continents/continent_detail.html'
    model = Continent
#    def get_context_data(self, *args, **kwargs):
#        continent = get_object_or_404(Continent, id=kwargs['id'])
#
#        return {'continent':continent}

def register_continent(request):
    form = RegisterContinentForm(request.POST or None)

    if form.is_valid():
        continent = form.save()
        return JsonResponse(
            {
                'name':continent.name,
                'color':continent.color,
                'population':continent.population
            }
        )
    return render(request, 'continents/register_continent.html',{'form':form})
