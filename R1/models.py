from django.db import models
from datetime import datetime
# Create your models here.
class signup(models.Model):
    User_name=models.CharField(max_length=50)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email_id=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    profession=models.CharField(max_length=50)

class table(models.Model):
    obj=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    off=models.CharField(max_length=50)
    idd=models.CharField(max_length=50)
    #ordered=models.CharField(max_length=50)

class orders(models.Model):
    buye= models.CharField(max_length=100)
    order=models.CharField(max_length=100)  
    p=models.CharField(max_length=100)
    dorn=models.CharField(max_length=100)