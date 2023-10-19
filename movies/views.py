from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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

    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    # movie = Movie.objects.get(id=movie_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
