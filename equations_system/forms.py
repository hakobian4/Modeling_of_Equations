from django import forms

class EquationForm(forms.Form):
    equation = forms.CharField(label="Equation",
                           error_messages={'required': 'Please check your equation'}, required=True)



