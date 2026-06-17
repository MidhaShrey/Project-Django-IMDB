from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete = models.CASCADE, related_name = 'watchlist')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

# Updating the Movie model to include more fields
# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=100)
#     isActive = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name