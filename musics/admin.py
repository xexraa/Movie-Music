from django.contrib import admin
from .models import AdditionalInfo, Music, Rate, Artist, Album


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['released']
    search_fields = ['title', 'description']
    
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['genre',]
    
    
@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['review',]
    

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name',]