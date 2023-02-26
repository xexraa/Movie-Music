from django.forms import ModelForm
from django import forms
from .models import AdditionalInfo, Music, Rate, Artist, Album


class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'description', 'released', 'single_by', 'img', 'sample']
        

class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['genre']
        

class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['stars', 'review']
        

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name']
        

class AlbumForm(ModelForm):  
    class Meta:
        model = Album
        fields = ['album_name',]