from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.db.models import Avg


from .models import AdditionalInfo, Music, Rate, Artist, Album
from .forms import AdditionalInfoForm, MusicForm, RateForm, ArtistForm, AlbumForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def all_songs(request):
    songs = Music.objects.annotate(avg_stars=Avg('rate__stars')).all()
    return render(request, 'musics/index.html', {'songs': songs})


@login_required
def new_song(request):
    music_form = MusicForm(request.POST or None, request.FILES or None)
    extras_form = AdditionalInfoForm(request.POST or None)

    if all((music_form.is_valid(), extras_form.is_valid())):
        music = music_form.save(commit=False)
        extras = extras_form.save()
        music.extras = extras
        music.save()
        return redirect(all_songs)
    
    return render(request, 'musics/music_form_new.html', {'music_form': music_form, 'extras_form': extras_form, 'new': True})     


@login_required
def edit_song(request, id):
    song = get_object_or_404(Music, pk=id)
    rate = Rate.objects.filter(music=song)
    artists = Artist.objects.filter(musics=song)
    albums = Album.objects.filter(musics=song)
    
    try:
        extras = AdditionalInfo.objects.get(music=song.id)
    except AdditionalInfo.DoesNotExist:
        extras = None
        
    if request.method == 'POST':
        music_form = MusicForm(request.POST or None, request.FILES or None, instance=song)
        extras_form = AdditionalInfoForm(request.POST or None, instance=extras)
        rate_form = RateForm(request.POST or None)
        artist_form = ArtistForm(request.POST or None)
        album_form = AlbumForm(request.POST or None)

        if 'stars' in request.POST:
            rate = rate_form.save(commit=False)
            rate.music = song
            rate.save()
            
        if 'album_name' in request.POST:
            new_album = album_form.save(commit=False)
            if new_album.album_name:
                song = music_form.save()
                new_album.save()
                new_album.musics.add(song)
        
        if 'first_name' in request.POST:
            new_artist = artist_form.save(commit=False)
            if new_artist.first_name or new_artist.last_name:
                song = music_form.save()
                new_artist.save()
                new_artist.musics.add(song)          
        
        if music_form.is_valid() and extras_form.is_valid():
            song = music_form.save(commit=False)
            extras = extras_form.save()
            song.extras = extras
            song.save()
            return redirect(all_songs)
    else:
        music_form = MusicForm(instance=song)
        extras_form = AdditionalInfoForm(instance=extras)
        rate_form = RateForm()
        artist_form = ArtistForm()
        album_form = AlbumForm()
    
    context = {
        'music_form': music_form,
        'extras_form': extras_form,
        'rates': rate,
        'rate_form': rate_form,
        'artists': artists,
        'artist_form': artist_form,
        'albums': albums,
        'album_form': album_form,
        'new': False
    }
    
    return render(request,'musics/music_form_edit.html', context=context)


@login_required
def delete_song(request, id):
    song = get_object_or_404(Music, pk=id)
    
    if request.method == "POST":
        song.delete()
        return redirect(all_songs)
    
    return render(request, 'confirmation.html', {'music_form': song})


@login_required
def description_song(request, id):
    song = get_object_or_404(Music, pk=id)
    rate = Rate.objects.filter(music=song)
    artists = Artist.objects.filter(musics=song)
    albums = Album.objects.filter(musics=song)
    extras = song.extras
    
    if extras is not None:
        genre = extras.get_genre_display()
    else:
        genre = 'Unknown'
        
    average_rating = rate.aggregate(Avg('stars'))['stars__avg']
    
    context = {
        'music': song,
        'rating': rate,
        'artists': artists,
        'albums': albums,
        'genre': genre,
        'average_rating': average_rating,
    }
    
    return render(request, 'musics/music_form_description.html', context=context)


@login_required
def review_song(request, id):
    song = get_object_or_404(Music, pk=id)
    rate_form = RateForm(request.POST or None)

    if request.method == 'POST' and rate_form.is_valid():
        rate = rate_form.save(commit=False)
        rate.music = song
        rate.save()
        messages.success(request, 'Your review has been added successfully.')
        return redirect(reverse('description_song', args=[song.id]))

    return render(request, 'musics/music_form_review.html', {'rate_form': rate_form})
