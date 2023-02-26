from rest_framework import viewsets
from .serializers import UserSerializer, MovieSerializer, MusicSerializer
from django.contrib.auth.models import User
from movies.models import Movie
from musics.models import Music


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

class MusicView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer