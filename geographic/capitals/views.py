from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterCapitalFormModel
from django.http import JsonResponse
from countries.models import Country

# Create your views here.

class Capitals(TemplateView):
    template_name = 'capitals/capitals.html'

def register_capital(request):
    countries=Country.objects.filter(city__isnull=True)
    form = RegisterCapitalFormModel(countries, request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        capital = Capital.objects.create(
            name=data['name'],
            description=data['description'],
            country=data['country']
        )
        return JsonResponse(
            {
                'name': capital.name,
                'description':capital.description,
                'country':capital.country
            }
        )
    return render(request, 'capitals/register_capital.html',{'form':form})
