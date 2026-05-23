from django.http import JsonResponse
from .models import Movie
# Create your views here.

def movieList(request):
    # Get all movies from the database
    movies = Movie.objects.all()
    # print(movies.values())  # returns queryset of dict
    # list(movies.values()) # conversion of queryset to list of dict
    data = {
        'movies': list(movies.values())}
    return JsonResponse(data, safe=False) # safe=False allows us to return non-dict objects as JSON response, in this case we are returning a list of dicts.

def movieDetails(request, primary_key):
    movie = Movie.objects.get(pk=primary_key)
    print(movie)
    data = {
        'id': movie.id,
        'name': movie.name,
        'description': movie.description,
        'isactive': movie.isactive
    }
    return JsonResponse(data)
