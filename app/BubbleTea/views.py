from django.shortcuts import render

# Create your views here.


def home_page(request):
    print(request.headers)
    return render(request, "index.html", {})

def login_page(request):
    print(request.headers)
    return render(request, "login.html", {})

def register_page(request):
    print(request.headers)
    return render(request, "register.html", {})

def profile_page(request):
    print(request.headers)
    return render(request, "profile.html", {})