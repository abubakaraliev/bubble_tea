from django.db import models

# Create your models here.

class Products(models.Model):
    id = models.IntegerField(primary_key=True),
    identifier = models.CharField(max_length=255),
    price = models.DecimalField(max_digits=10, decimal_places=2),
    is_available = models.BooleanField(default=True),