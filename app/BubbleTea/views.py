from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home_page(request):
    # print(request.headers)
    return render(request, "index.html", {})


def register_page(request):
    # print(request.headers)
    form = CreateUserForm()
    
    if  request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('login')
    
    context = {'form':form}
    return render(request, "register.html", context)

def login_page(request):
    # print(request.headers)
    form = LoginUserForm()
    
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            print(form.get_user())
            login(request, form.get_user())
            return redirect('profile')
        else:
            form = LoginUserForm()
            messages.info(request, 'Email OR Password is incorrect !')
    context = {'form':form}
    return render(request, "login.html", context)

def profile_page(request):
    # print(request.headers)
    return render(request, "profile.html", {})