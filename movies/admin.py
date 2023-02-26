from django.contrib import admin
from .models import Actor, AdditionalInfo, Movie, Rate


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['premiere']
    search_fields = ['title', 'description']
    
    
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['genre',]
    
    
@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['review',]

