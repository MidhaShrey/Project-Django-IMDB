from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.id} | {self.name}'

class WatchList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete = models.CASCADE, related_name = 'watchlist')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} | {self.title}'
    
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID:{self.id} | {self.rating} | {self.watchlist.title} | {self.watchlist.platform.name}"

# Updating the Movie model to include more fields
# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=100)
#     isActive = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name