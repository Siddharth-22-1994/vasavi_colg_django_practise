from django import forms

class form_function(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField()
    email = forms.EmailField()
    