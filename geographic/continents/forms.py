from django import forms
from colorful.fields import RGBColorField

class RegisterContinentForm(forms.Form):
    name = forms.CharField(label='nombre')
    population = forms.IntegerField(label='poblacion',required=False)
    color = RGBColorField()
