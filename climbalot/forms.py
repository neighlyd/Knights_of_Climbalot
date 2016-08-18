from django import forms
from django.forms import ModelForm
from climbalot.models import Session
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget

class SessionInputForm(ModelForm):
    session_date = forms.DateField(localize = True)

    class Meta:
        model = Session
        fields = ['session_date']
