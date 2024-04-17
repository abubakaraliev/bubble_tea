from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, LoginUserForm, ProfileUserForm
from django.contrib import messages
from django.contrib.auth import login, logout

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
    form = LoginUserForm()
    
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            user_profile_data = {
                'username': user.username,
                'email': user.email
            }
            request.session['user_profile_data'] = user_profile_data
            return redirect('profile')
        else:
            form = LoginUserForm()
            messages.info(request, 'Email OR Password is incorrect !')
            
    context = {'form':form}
    return render(request, "login.html", context)

def profile_page(request):
    # print(request.headers)
    
    user_profile_data = request.session.get('user_profile_data', {})
    if request.method == 'POST':
        form = ProfileUserForm(data=request.POST)
        if form.is_valid():
            user_profile_data.update(form.cleaned_data)
            request.session['user_profile_data'] = user_profile_data
            messages.success(request, 'Profile has been updated !')
            return redirect('profile')
    else:
        form = ProfileUserForm(initial=user_profile_data)
    context = {'form':form }
    return render(request, "profile.html", context)