from django.shortcuts import render, redirect
from credapp.forms import Empform
from credapp.models import Employee

# Create your views here.

def createemp(request):
    if request.method=="POST":
        form=Empform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('createform')
    
    form = Empform()
    return render(request, 'credform.html', {'form': form})

def alldata(request):
    datas = Employee.objects.all()
    print(datas)
    return render(request, "displaydata.html", {"data": datas})

def updateemp(request, id):
    employe = Employee.objects.get(pk=id)
    form = Empform(request.POST or None, instance=employe)
    
    if form.is_valid():
        form.save()
        return redirect('alldata')
    return render(request, 'credform.html', {"form": form})

def delemp(request, id):
    emp = Employee.objects.get(pk=id) 
    emp.delete()   
    
    return redirect(alldata)