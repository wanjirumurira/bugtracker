from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from . models import CustomUser

# Create your views here.
def index(request):
    return render (request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
                user = CustomUser.objects.create_user(email=email,username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect ('register')
    return render (request,'register.html')

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.info(request, "Invalid Password or Username")
            return redirect('login')
    return render(request,'signin.html')
        
   
