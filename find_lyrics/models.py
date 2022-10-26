from django.db import models

# Create your models here.
class profile(models.Model):
    song_name=models.CharField(max_length=50)
    artist_name=models.CharField(max_length=50)
    