from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, LoginUserForm, ProfileUserForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse, JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt


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

def shop_page(request):
    # print(request.headers)
    return render(request, "shop.html", {})

@csrf_exempt
def products(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products')
        data = cursor.fetchall()
        print((data))
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in data]
        to_json = json.dumps(data, indent=2)
        print(to_json)
        return HttpResponse(to_json, content_type='application/json')
    
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body['identifier'])
        cursor = connection.cursor()
        cursor.execute('INSERT INTO products (identifier, price) VALUES (%s, %s)', [body['identifier'], body['price']])
        return HttpResponse('Product created', content_type='application/json')

@csrf_exempt
def get_one_product(request, id):
    print(id)
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products WHERE id = %s', [id])
        data = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in data]
        
        to_json = json.dumps(data, indent=2)
        print(to_json)
        return HttpResponse(to_json, content_type='application/json') #CREATE JSON
    elif request.method == 'DELETE':
        cursor = connection.cursor()
        cursor.execute('DELETE FROM products WHERE id = %s', [id])
        return HttpResponse('Product deleted', content_type='application/json')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cursor = connection.cursor()
        cursor.execute('UPDATE products SET identifier = %s, price = %s WHERE id = %s', [body['identifier'], body['price'], id])
        return HttpResponse('Product updated', content_type='application/json')