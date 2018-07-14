from django import forms
from .models import Capital
from countries.models import Country

class RegisterCapital(forms.Form):
    name = forms.CharField(label='Nombre')
    description = forms.CharField(label='Descripción')
    country = forms.ModelChoiceField(queryset=Country.objects.all())

class RegisterCapitalFormModel(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['country'].queryset=countries

    name = forms.CharField(label='Nombre')
    description = forms.CharField(label='Descripción')
    country = forms.ModelChoiceField(queryset=Country.objects.all())
