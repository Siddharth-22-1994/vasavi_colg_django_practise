from django.shortcuts import render
from modelstoform.models import employee

# Create your views here.

def viewdetails(request):
    details = employee.objects.all()
    return render(request, 'contact.html', {"data":details})