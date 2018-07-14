from django import forms
from .models import Person
from countries.models import Country

class RegisterPersonFormModel(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'name',
            'last_name',
            'born_date',
            'phone_number',
            'nationalities',
            'is_active',
        ]
    def __init__(self, *args, **kwargs):
        super(RegisterPersonFormModel,self).__init__(*args, **kwargs)
        self.fields['born_date'].widget.attrs.update({'class':'datepicker'})
