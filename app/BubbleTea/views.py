from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .forms import LoginUserForm, CreateUserForm, InformationsUserForm
import bcrypt
import jwt
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "index.html", {})

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Users(username, email, password) VALUES (%s, %s, %s)",
                        [username, email, hashed_password.decode('utf-8')]
                    )
                
                messages.success(request, f'Account created for {username}')
                return redirect('login')
            
            else:
                form = CreateUserForm()
                messages.info(request, 'Wrong inputs!')
                
        except Exception:
            messages.error(request, 'An error occurred.')

    context = {'form': form}
    return render(request, "register.html", context)

def login(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Users WHERE username = %s", [username])
                user = cursor.fetchone()
            if user:
                hashed_password = user[1]
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                    payload = {'username': username}
                    secret_key = "secret"
                    algorithm = "HS256"

                    encoded_token = jwt.encode(payload, secret_key, algorithm=algorithm)
                    
                    response = redirect('account')
                    response.set_cookie('access_token', encoded_token)
                    return response
                else:
                    messages.error(request, 'Incorrect password!')
            else:
                messages.error(request, 'Incorrect username or password!')
                
        else:
            messages.error(request, 'Invalid form submission!')

    context = {'form': form}
    return render(request, "login.html", context)

def account(request):
    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect('login')

    secret_key = "secret"
    algorithm = "HS256"

    try:
        payload = jwt.decode(access_token, secret_key, algorithms=[algorithm])
        username = payload['username']

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE Users SET email = %s, password = %s WHERE username = %s", [email, hashed_password.decode('utf-8'), username])
                messages.success(request, 'Profile updated successfully')
                return redirect('account')
            
            else:
                form = CreateUserForm()
                messages.info(request, 'Wrong inputs!')
            
        context = {'form': form}
        return render(request, "account.html", context)

    except jwt.ExpiredSignatureError:
        messages.error(request, 'Your session has expired. Please log in again.')
        return redirect('login')

    except jwt.InvalidTokenError:
        messages.error(request, 'Invalid token. Please log in again.')
        return redirect('login')

def delivery(request):
    form = InformationsUserForm()

    if request.method == 'POST':
        form = InformationsUserForm(request.POST)
        if form.is_valid():
            lastname = form.cleaned_data.get('lastname')
            firstname = form.cleaned_data.get('firstname')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            postcode = form.cleaned_data.get('postcode')
            city = form.cleaned_data.get('city')
            
            print(lastname, firstname, phone, address, postcode, city)

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Users_informations(lastname, firstname, phone, address, postcode, city) VALUES (%s, %s, %s ,%s, %s, %s)",
                    [lastname, firstname, phone, address, postcode, city]
                )
            
            messages.success(request, f' delivery informations have been registered for {firstname}')
            return redirect('delivery')
            
        else:
            form = InformationsUserForm()
            messages.info(request, 'Wrong inputs!')

    context = {'form': form}
    return render(request, "delivery.html", context)

@csrf_exempt
def products(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Products')
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
        cursor.execute('INSERT INTO Products (identifier, price) VALUES (%s, %s)', [body['identifier'], body['price']])
        return HttpResponse('Product created', content_type='application/json')

@csrf_exempt
def get_one_product(request, id):
    print(id)
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Products WHERE id = %s', [id])
        data = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in data]
        
        to_json = json.dumps(data, indent=2)
        print(to_json)
        return HttpResponse(to_json, content_type='application/json') #CREATE JSON
    elif request.method == 'DELETE':
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Products WHERE id = %s', [id])
        return HttpResponse('Product deleted', content_type='application/json')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cursor = connection.cursor()
        cursor.execute('UPDATE Products SET identifier = %s, price = %s WHERE id = %s', [body['identifier'], body['price'], id])
        return HttpResponse('Product updated', content_type='application/json')
