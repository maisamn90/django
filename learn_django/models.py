from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description= models.CharField(max_length=200)
    
    def __str__(self):
        return (self.name)

class Visitor (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return (self.name)

class CustomUser (AbstractUser):
    address = models.CharField(max_length = 300 , null= True)
    is_employee = models.BooleanField(default= False)
    is_customer = models.BooleanField(default= False)
    # is_active = models.BooleanField(default= False)