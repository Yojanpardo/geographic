from django import forms

class RegisterContinentForm(forms.Form):
    name = forms.CharField(label='nombre')
    population = forms.IntegerField(label='poblacion',required=False)
    color = forms.CharField(label='Color en exadecimal')
