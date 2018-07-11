from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Country
from .forms import RegisterCountryForm

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

def register_country(request):
    form = RegisterCountryForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        country = Country.objects.create(
            name = data['name'],
            code = data['code'],
            description = data['description'],
            classification = data['classification'],
            continent = data['continent']
        )
        return JsonResponse(
            {
                'name':country.name,
                'code':country.code,
                'classification':country.classification
            }
        )
    return render(request, 'countries/register_country.html',{'form':form})
