from django.urls import path
from watchlist_app.views import movieList, movieDetails

urlpatterns = [
    path('list/', movieList, name='movie-list'),
    path('<int:primary_key>', movieDetails, name='movie-details'),
]
