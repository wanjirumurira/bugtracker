from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import *

# Create your views here.
def index(request):
    new_project = Project.objects.all()
    
   
    
    context = {'new_project':new_project}

    return render (request,'index.html',context)

def create_project(request):
    if request.method == 'POST':
        # project_name = request.POST["projectname"]
        # contributors = request.POST.getlist("contributors")

        # project_description = request.POST["projectdescription"]
        
        return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username is Already Taken')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email is Already Taken')
            else:
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
            return redirect('index')
        else:
            messages.info(request, "Invalid Password or Username")
            return redirect('login')
    return render(request,'signin.html')
        
def sign_out(request):
    logout(request)
    return redirect('login')
    
