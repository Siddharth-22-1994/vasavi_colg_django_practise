from django import forms
from credapp.models import Employee


class Empform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('E_name', "E_id","E_email", "E_salary")