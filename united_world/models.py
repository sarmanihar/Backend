from django.db import models
#from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    Question = models.CharField(max_length=15)
    Answer1 = models.CharField(max_length=15)
    Answer2 = models.CharField(max_length=15)
    Answer3 = models.CharField(max_length=15)
    Answer4 = models.CharField(max_length=15)
    S_Answer=models.CharField(max_length=15)

class Post(models.Model):
    ans= models.CharField(max_length=300, unique=True)

