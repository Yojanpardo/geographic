from django.shortcuts import render
from django.http import HttpResponse #Se importa el objeto HttpResponse para poder retornar la vista.
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render(request, 'continents/home.html')

class Continents(TemplateView):

    template_name='continents/continents.html'

    def get_context_data(self, *args, **kwargs):
        africa = {'name':'África','description':'Hot'}
        antartida = {'name':'Antártida', 'description':'Cold'}
        america = {'name':'América','description':'new world'}
        asia = {'name':'Asia','description':'Chinos'}
        europa = {'name':'Europa','description':'conquers'}
        oseania = {'name':'Oseania','description':'kangaroos'}
        continents=[africa,antartida,america,asia,europa,oseania]
        return {'continents':continents}
