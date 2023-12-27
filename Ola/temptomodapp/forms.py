from django import forms
from temptomodapp.models import staff_model
from django.core import validators

class empfrom(forms.ModelForm):
    class Meta:
        model = staff_model
        # fields = ["name", "age", "email", "Gender","phone"]
        # or
        fields= '__all__'