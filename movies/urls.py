from django.contrib import admin
from django.urls import path
from .views import all_movies, new_movie, edit_movie, delete_movie, description_movie, review_movie


urlpatterns =[
    path('', all_movies, name='all_movies'),
    path('new/', new_movie, name='new_movie'),
    path('edit/<int:id>/', edit_movie, name='edit_movie'),
    path('delete/<int:id>/', delete_movie, name='delete_movie'),
    path('full/<int:id>/', description_movie, name='description_movie'),
    path('review/<int:id>/', review_movie, name='review_movie'),
]