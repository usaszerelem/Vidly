from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def index(request):
    # Database abstraction APIs:

    # Filtering is also possible like this
    # Movie.objects.filter(release_year=1985)

    # To get a single movie
    # Movie.objects.get(id=1)

    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])

    output = render(request, 'movies/index.html', {'movies': movies})
    return HttpResponse(output)
