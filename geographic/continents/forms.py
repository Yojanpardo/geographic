from django import forms
from colorful.fields import RGBColorField
from .models import Continent

class RegisterContinentModelForm(forms.ModelForm):

    class Meta:
        model = Continent
        fields = ['name','population','color']

#    name = forms.CharField(label='nombre')
#    population = forms.IntegerField(label='poblacion',required=False)
#    color = RGBColorField()
