from django.contrib import messages
from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User,auth
from .models import *

from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                print("user created")
        else:
            print("not match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid details")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
#return render(request,'logout.html')
