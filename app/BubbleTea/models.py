from django.db import models
import uuid

class newUser(models.Model):
    # user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

class loginForm(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

class accountUpdate(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

class userInformations (models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
# Create your models here.

class Products(models.Model):
    id = models.IntegerField(primary_key=True),
    identifier = models.CharField(max_length=255),
    price = models.DecimalField(max_digits=10, decimal_places=2),
    is_available = models.BooleanField(default=True),
