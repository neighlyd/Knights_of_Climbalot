from django import forms
from django.forms import ModelForm, inlineformset_factory
from climbalot.models import Session, C_Routes
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget

class SessionInputForm(ModelForm):
    session_date = forms.DateField(localize = True)

    class Meta:
        model = Session
        fields = ['session_date', 'gym', 'extra_points', 'workout', 'quest_one_id', 'quest_one_attempts',
                'quest_two_id', 'quest_two_attempts', 'quest_three_id', 'quest_three_attempts',
                'session_exp']

C_Route_Formset = inlineformset_factory(Session, C_Routes, fields=('yellow', 'green', 'red', 'blue', 'orange', 'purple', 'black'),)
