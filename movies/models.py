from django.db import models
from django.core.validators import MaxValueValidator


class AdditionalInfo(models.Model):
    GENRE = {
        (0, 'Action'),
        (1, 'Horror'),
        (2, 'Comedy'),
        (3, 'Sci-Fi'),
        (4, 'Drama'),
    }   
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE)
    

class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    description = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    duration = models.PositiveSmallIntegerField(default=0)
    img = models.ImageField(upload_to='img', null=True, blank=True)
    extras = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title_with_date()
    
    def title_with_date(self):
        return f"{self.title} {(self.premiere)}"
    

class Rate(models.Model):
    review = models.TextField(default='', blank=True, max_length=500)
    stars = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Actor(models.Model):
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    movies = models.ManyToManyField(Movie, related_name='actors')
