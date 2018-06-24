from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def countries(request):
    return HttpResponse('Paises del mundo')
