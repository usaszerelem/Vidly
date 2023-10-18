from django.db import models
from django.utils import timezone

# Create your models here.
# The __str__ magic function override is needed so that the genre
# is correctly displayed when adding a move in the admin panel

class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    