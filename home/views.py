from collections import UserDict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages
# Create your views here.


def thanks1(requests):
   return render(requests,'thanks1.html')

def about(requests):
   return render(requests,'about.html')

def thanks2(requests):
   return render(requests,'thanks2.html')

def thanks(requests):
   return render(requests,'thanks.html')

def create(request):
     if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        lastname =request.POST.get('NUMBER')
        email =request.POST.get('email')
        
      #   print(username,password,)
        user = User.objects.create_user(username=username,email=email,last_name =lastname, password=password)
        user.save()
        messages.success(request,'YOUR ACCOUNT IS CREATED PLEASE LOGIN NOW')
        return render(request,'login.html')

     return render(request,'create.html')


def index(request):
    print(request.user)
    if request.user.is_anonymous:
     return redirect("/login")
    return render(request, 'index.html')
    #  return HttpResponse('<h1>Page not')
 
def logi(request):
     if request.method == "POST":
          
        username = request.POST.get('username')
        password = request.POST.get('password')

     #    print(usern,passw,123)
        user = authenticate(username= username, password=password)
        if user is not None:
             # A backend authenticated the credentials
             print(password,12344221)
             login(request,user)
             
             return  redirect("/")
     
        else:
              
              messages.warning(request,'INVALID')
              return render(request, 'login.html')
         # No backend authenticated the credentials

     return render(request, 'login.html')


def logou(request):
    logout(request)
    messages.success(request,'YOU LOGGED OUT SUCCESSFULLY')
    return redirect("/login")

def cre(request):
   return redirect("create.html")
   