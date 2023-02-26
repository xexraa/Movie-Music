from django.contrib.auth.models import User
from rest_framework import serializers
from movies.models import Movie
from musics.models import Music


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
        
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'premiere']
        

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'description', 'released', 'single_by']