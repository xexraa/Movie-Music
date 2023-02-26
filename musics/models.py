from django.db import models
from django.core.validators import MaxValueValidator, FileExtensionValidator
from .validators import MaxFileSizeValidator



class AdditionalInfo(models.Model):
    GENRE = {
        (0, 'Other'),
        (1, 'Hip hop'),
        (2, 'Rock'),
        (3, 'Rhythm and blues'),
        (4, 'Soul'),
        (5, 'Country'),
        (6, 'Funk'),
        (7, 'Folk'),
        (8, 'Disco'),
        (9, 'Electronic'),
        (10, 'Blues'),
        (11, 'Classical'),
        (12, 'Pop'),
    }   
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE)


class Music(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    description = models.TextField(default='')
    released = models.DateField(null=True, blank=True)
    single_by = models.CharField(max_length=64, blank=True, unique=False)
    extras = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='img', null=True, blank=True)
    sample = models.FileField(
        upload_to='samples', 
        null=True, 
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp3', 'wav']),
            MaxFileSizeValidator(max_size=10 * 1024 * 1024)  # 10 MB
        ]
    )
    
    def __str__(self) -> str:
        return f"{self.title}"
    
      
    
class Rate(models.Model):
    review = models.TextField(default='', blank=True, max_length=500)
    stars = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    music = models.ForeignKey(Music, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Artist(models.Model):
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    musics = models.ManyToManyField(Music, related_name='artists')
    
    
class Album(models.Model):
    album_name = models.CharField(max_length=64, null=True, blank=True)
    musics = models.ManyToManyField(Music, related_name='albums')
    