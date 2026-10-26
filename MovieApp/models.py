from django.db import models

# Create your models here.
class MovieDb(models.Model):    

    title=models.CharField(max_length=100)
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    release_year=models.IntegerField()
    rating=models.FloatField()
    duration=models.IntegerField()
    description=models.TextField(blank=True)
    language=models.CharField(max_length=100)
