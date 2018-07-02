from django.shortcuts import render
from django.http import HttpResponse #Se importa el objeto HttpResponse para poder retornar la vista.
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Continent
# Create your views here.

def home(request):
    return render(request, 'continents/home.html')

class Continents(ListView):
    model = Continent
    template_name='continents/continents.html'

class ContinentDetailView(TemplateView):
    template_name = 'continents/continent_detail.html'

    def get_context_data(self, *args, **kwargs):
        code_id = kwargs['id']
        return {'id':code_id}
