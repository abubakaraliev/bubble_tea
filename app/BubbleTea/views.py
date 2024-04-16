from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from .forms import CreateUserForm

def home_page(request):
    # print(request.headers)
    return render(request, "index.html", {})

def login_page(request):
    # print(request.headers)
    return render(request, "login.html", {})

def register_page(request):
    # print(request.headers)
    form = CreateUserForm()
    
    if  request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, "register.html", context)

def profile_page(request):
    # print(request.headers)
    return render(request, "profile.html", {})