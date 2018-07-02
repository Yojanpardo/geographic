from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Country

# Create your views here.

class Countries(TemplateView):
    template_name='countries/countries.html'

class CountryDetailView(TemplateView):
    template_name='countries/country_detail.html'

    def get_context_data(self, *args, **kwargs):
        code = kwargs['code']
        return {'code':code}

class SearchCountry(ListView):
    template_name = 'countries/search.html'
    model = Country

    def get_queryset(self):
        query = self.kwargs['query']
        return Country.objects.filter(name__contains=query)
