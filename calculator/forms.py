from django import forms

class MathEquationForm(forms.Form):
    input = forms.CharField(label='Enter a math equation', max_length=10)