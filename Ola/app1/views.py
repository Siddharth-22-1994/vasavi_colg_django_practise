from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.forms import form_function


# Create your views here.
# def home(request):
#     return HttpResponse("<h1 style='color:red;'> hello world </h1>")

def home(request):
# def home(request, name):
    # context = {
    #     "name":"siddharth"
    # }
    #! or
    name = "sidhu"
    # return render(request, "home.html", context)
    # or
    
    # print(request.GET.items())
    return render(request, "home.html")
    return HttpResponse(request.GET.items())

    

# def contact(request, name, place, age):
#     name = name
#     place = place
    
#     if age<18:
#         return render(request, "home.html", {"name":name})
#     else:
#         return render(request, "contact.html", {"fname":name})

def contact(request):
    if request.method == 'POST':
      username= request.POST["Name"]
      age = request.POST["Age"]
      dict = {
         'name': username,
         'age': age
      }
      return render(request, 'contact.html', dict)
  
def formview(request):
    if request.method=="POST":
        form = form_function(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            
            print(type(name), age)
            
    form = form_function()
    return render(request, "formhtml.html", {"form": form})