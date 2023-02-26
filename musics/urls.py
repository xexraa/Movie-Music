from django.contrib import admin
from django.urls import path
from .views import all_songs, new_song, edit_song, delete_song, description_song, review_song


urlpatterns =[
    path('songs/', all_songs, name='all_songs'),
    path('songs/new/', new_song, name='new_song'),
    path('songs/edit/<int:id>/', edit_song, name='edit_song'),
    path('songs/delete/<int:id>/', delete_song, name='delete_song'),
    path('songs/full/<int:id>/', description_song, name='description_song'),
    path('songs/review/<int:id>/', review_song, name='review_song'),
]