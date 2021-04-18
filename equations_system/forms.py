from django import forms
from durationwidget.widgets import TimeDurationWidget


class EquationForm(forms.Form):
    equation = forms.CharField(label="Equation",
                           error_messages={'required': 'Please check your equation'})

