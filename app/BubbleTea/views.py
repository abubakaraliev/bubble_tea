from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .forms import LoginUserForm, CreateUserForm, AccountUserForm ,ProfileUserForm
import jwt

def home(request):
    return render(request, "index.html", {})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Users(username, email, password) VALUES (%s, %s, %s)", [username, email, password])
            
            messages.success(request, f'Account created for {username}')
            return redirect('login')

        else:
            form = CreateUserForm()
            messages.info(request, 'Wrong inputs !')
    context = {'form': form}
    return render(request, "register.html", context)

def login(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Users WHERE username = %s", [username])
                user = cursor.fetchone()
            if user:
                payload = {'username': username}
                secret_key = "secret"
                algorithm = "HS256"

                encoded_token = jwt.encode(payload, secret_key, algorithm=algorithm)
                print("--- TOKEN ---\n", encoded_token)
                print("--- TOKEN ---")
                
                response = redirect('profile')
                response.set_cookie('access_token', encoded_token)
                return response
        else:
            messages.error(request, 'Email or Password is incorrect!')

    context = {'form': form}
    return render(request, "login.html", context)

def profile(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Users SET email = %s, password = %s WHERE username = %s", [email, password, username])
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')

    context = {'form': form}
    return render(request, "profile.html", context)