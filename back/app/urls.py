"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from BubbleTea.views import (
    home,
    account,
    delivery,
    register,
    remove,
    login,
    products,
    get_one_product,
)

urlpatterns = [
    path('', home),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('account-settings/', account, name="account"),
    path('delete/<str:username>', remove, name="remove"),
    path('delivery-informations/', delivery, name="delivery"),
    path('admin/', admin.site.urls),
    
    # products routes
    path('products/', products, name='products'),
    path('products/<int:id>', get_one_product, name='get_one_product'),
]
