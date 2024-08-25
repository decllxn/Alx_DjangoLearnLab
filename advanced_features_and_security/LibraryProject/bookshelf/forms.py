from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, strip=True)

from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)