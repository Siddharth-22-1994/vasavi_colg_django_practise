from django.shortcuts import render

# Create your views here.
def home(request, name, age, place):
    fname=""
    if request.method == "POST":
        fname = request.POST['name']
        # return render(request, 'index.html', {"fname":fname})
    
    context = {
        "fname":fname,
        "name":name,
        "age":age,
        "place":place
        }
    return render(request, 'index.html', context)

# def home(request):
#     return render(request, 'index.html')


def show(request):
    if request.method=='POST':
        value = request.POST["name"]
        return render(request, 'show.html', {"val":value})
    
