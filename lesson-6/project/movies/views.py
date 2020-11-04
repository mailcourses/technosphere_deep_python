from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer

def movie_view(request):
    return HttpResponse('Hello!')

def movie_html_view(request):
    movies = Movie.objects.all()
    return render(request, 'base.html', {'title': 'Memento', 'movies': movies})

class MovieView(APIView):
    def get(self, requet):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response({'movies': serializer.data})
