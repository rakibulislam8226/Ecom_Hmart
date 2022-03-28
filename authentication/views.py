from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register(request):
    if request.method=="POST" or request.method=="post":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        customer=User.objects.create_user(username,email,password1)
        customer.save()
        return redirect('register')
    return render(request,'auth/auth.html')

def userlogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    return render(request,'auth/auth.html')


def logoutuser(request):
    logout(request)
    return redirect('home')