from django.contrib import admin
# from watchlist_app.models import Movie
# Register your models here.
# admin.site.register(Movie)

from watchlist_app.models import WatchList, StreamPlatform
admin.site.register(WatchList)
admin.site.register(StreamPlatform)