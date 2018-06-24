from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class Countries(TemplateView):
    template_name='countries/countries.html'

    def get_context_data(self, *args, **kwargs):
        countries = ['Afganistán','Argentina','Brasil','Chile','Colombia','Dember','Dinamarca','Estocolmo']
        return {'countries':countries}
