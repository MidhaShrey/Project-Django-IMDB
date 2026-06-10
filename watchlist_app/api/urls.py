from django.urls import path
from watchlist_app.api.views import *

# Class Based Views
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:primary_key>', MovieDetailsAV.as_view(), name='movie-details'),
]

# Function Based Views
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:primary_key>', movie_details, name='movie-details'),
# ]
