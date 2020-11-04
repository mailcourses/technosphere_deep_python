from django.urls import path, include

from movies.views import movie_view, movie_html_view, MovieView

urlpatterns = [
    path('', movie_view),
    path('memento/', movie_html_view),
    path('api/', MovieView.as_view()),
]
