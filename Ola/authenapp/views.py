from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages #import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=="POST":
        fname = request.POST['firstname']
        lname =request.POST['lastName']
        email=request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Please check the password" )
            return render(request, "register.html")
            
        
        data =User.objects.create(first_name=fname, last_name=lname, email=email, username=username, password=password1)
        data.save()
        return render(request, "login.html")
    return render(request, 'register.html')

# link --> https://www.youtube.com/watch?v=dLcDNKf6DO0

def login_request(request):
    if request.method=="POST":
        username = request.POST["Username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successfull" )
            return render(request, "products.html")
        else:
            messages.success(request, "Please check the Credntials" )
            return render(request, "login.html")
    return render(request, "login.html")

def logout_user(request):
    auth.logout(request)
    return render(request, "register.html")