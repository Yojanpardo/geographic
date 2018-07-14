from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterPersonFormModel
from django.http import JsonResponse
from .models import Person
# Create your views here.

class People(TemplateView):
    template_name = 'people/people.html'

def register_person(request):
    form = RegisterPersonFormModel(request.POST or None)

    if form.is_valid():
        person = form.save()
        return JsonResponse(
            {
                'name':person.name
            }
        )
    return render(request,'people/register_person.html',{'form':form})
