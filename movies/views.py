from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.db.models import Avg

from .models import AdditionalInfo, Actor, Movie, Rate
from .forms import AdditionalInfoForm, ActorForm, MovieForm, RateForm


def all_movies(request):
    movies = Movie.objects.annotate(avg_stars=Avg('rate__stars')).all()
    return render(request, 'movies/index.html', {'movies': movies})


@login_required
def new_movie(request):
    movie_form = MovieForm(request.POST or None, request.FILES or None)
    extras_form = AdditionalInfoForm(request.POST or None)
    
    if all((movie_form.is_valid(), extras_form.is_valid())):
        movie = movie_form.save(commit=False)
        extras = extras_form.save()
        movie.extras = extras
        movie.save()
        return redirect(all_movies)
    
    return render(request, 'movies/movie_form_new.html', {'movie_form': movie_form, 'extras_form': extras_form, 'new': True})


@login_required
def edit_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    rate = Rate.objects.filter(movie=movie)
    actors = Actor.objects.filter(movies=movie)
    
    try:
        extras = AdditionalInfo.objects.get(movie=movie.id)
    except AdditionalInfo.DoesNotExist:
        extras = None
        
    if request.method == 'POST':
        movie_form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
        extras_form = AdditionalInfoForm(request.POST or None, instance=extras)
        rate_form = RateForm(request.POST or None)
        actor_form = ActorForm(request.POST or None)

        if 'stars' in request.POST:
            rate = rate_form.save(commit=False)
            rate.movie = movie
            rate.save()
        elif 'first_name' in request.POST:
            new_actor = actor_form.save(commit=False)
            if new_actor.first_name or new_actor.last_name:
                movie = movie_form.save()
                new_actor.save()
                new_actor.movies.add(movie)

        if movie_form.is_valid() and extras_form.is_valid():
            movie = movie_form.save(commit=False)
            extras = extras_form.save()
            movie.extras = extras
            movie.save()
            return redirect(all_movies)
    else:
        movie_form = MovieForm(instance=movie)
        extras_form = AdditionalInfoForm(instance=extras)
        rate_form = RateForm()
        actor_form = ActorForm()
    
    context = {
        'movie_form': movie_form,
        'extras_form': extras_form,
        'rates': rate,
        'rate_form': rate_form,
        'actors': actors,
        'actor_form': actor_form,
        'new': False
    }
    
    return render(request,'movies/movie_form_edit.html', context=context)



@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    
    if request.method == "POST":
        movie.delete()
        return redirect(all_movies)
    
    return render(request, 'confirmation.html', {'movie_form': movie})


@login_required
def description_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    rate = Rate.objects.filter(movie=movie)
    actors = Actor.objects.filter(movies=movie)
    average_rating = rate.aggregate(Avg('stars'))['stars__avg']
    
    context = {
        'movie': movie,
        'rating': rate,
        'actors': actors,
        'average_rating': average_rating
    }
    
    return render(request, 'movies/movie_form_description.html', context=context)


@login_required
def review_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    rate_form = RateForm(request.POST or None)

    if request.method == 'POST' and rate_form.is_valid():
        rate = rate_form.save(commit=False)
        rate.movie = movie
        rate.save()
        messages.success(request, 'Your review has been added successfully.')
        return redirect(reverse('description_movie', args=[movie.id]))

    return render(request, 'movies/movie_form_review.html', {'rate_form': rate_form})
