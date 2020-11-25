from django.db import models
from django.db import IntegrityError

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=10, unique=True)
    movie_type = models.CharField(max_length=10)
    released_country = models.CharField(max_length=10)
    movies_characters = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    released_date = models.CharField(max_length=10)