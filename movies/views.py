from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def detalle(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'detalle.html', {'movie': movie})