from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class Countries(TemplateView):
    template_name='countries/countries.html'

class CountryDetailView(TemplateView):
    template_name='countries/country_detail.html'

    def get_context_data(self, *args, **kwargs):
        code = kwargs['code']
        return {'code':code}
