from django.shortcuts import render
from account.forms import form_function

# Create your views here.

def home(request,name, age, place):
    if request.method == "POST":
        fname = request.POST['name']
        fage = request.POST['age']
        
        context = {
            "fname":fname, 
            "fage":fage
        }
        return render(request, "index.html", context)
     
    # name = "sidhu"
    # age = 29
    # phone = 9878787676
    # return render(request, 'index.html', {"fname":name, "age":age, "phone":phone})
            # ! or
    # data = {
    #     "name": "sidhu",
    #     "age": 29,
    #     "place": 'cbe'
    # }
    
    
    var_name = name
    age = age
    place = place
    
    return render(request, 'index.html', {"name1": var_name, 'age':age, 'place':place})

def formview(request):
    if request.method=="POST":
        form = form_function(request.POST or None)
        if form.is_valid():
            dict = form.cleaned_data
            context = {
                "name":dict['name'],
                "age":dict["age"],
                "email":dict["email"]
            }
            return render(request, 'ans.html', context)
        
    form = form_function()
    return render(request, 'formhtml.html', {'form':form})

count = 0
def answer(request):
    global count
    count+=1
    print(count)
    return render(request, 'ans.html', {"count":count})
    
