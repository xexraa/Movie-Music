from django.forms import ModelForm
from .models import Actor, Movie, AdditionalInfo, Rate


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'premiere', 'duration', 'img']
        

class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['genre']
        

class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['stars', 'review']
        

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']