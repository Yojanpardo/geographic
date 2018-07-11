from django import forms
from continents.models import Continent
from .models import Country

class RegisterCountryForm(forms.Form):
    continents = Continent.objects.all()
    name = forms.CharField(label='Country name')
    code = forms.CharField(max_length=3,label='Code')
    description = forms.CharField(max_length=255,label='Description')
    classification = forms.ChoiceField(choices=Country().CLASSIFICATION,label='classification')
    continent = forms.ModelChoiceField(queryset=continents,label='continent')

#class RegisterModelCountryForm(forms.ModelForm):
#    class Meta:
#        model = Country
#        fields = ['name','code','description','classification','continent']
