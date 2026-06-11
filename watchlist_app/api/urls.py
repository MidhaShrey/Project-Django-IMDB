from django.urls import path
from watchlist_app.api.views import *

urlpatterns = [
    path('stream/list/', StreamPlatformAV.as_view(), name='streamplatform-list'),
    path('stream/detail/<int:primary_key>/', StreamPlatformDetailsAV.as_view(), name='streamplatform-details'),
    path('list/', WatchListAV.as_view(), name='watchlist-list'),
    path('list/detail/<int:primary_key>/', WatchListDetailsAV.as_view(), name='watchlist-details'),
]

# Class Based Views
# urlpatterns = [
#     path('list/', MovieListAV.as_view(), name='movie-list'),
#     path('detail/<int:primary_key>/', MovieDetailsAV.as_view(), name='movie-details'),
# ]

# Function Based Views
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('detail/<int:primary_key>/', movie_details, name='movie-details'),
# ]
