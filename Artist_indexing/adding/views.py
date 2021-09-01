from django.shortcuts import render
from adding.models import Musician,Album
from adding import forms

from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    album_list = Album.objects.order_by('release_date')
    diction={'title': 'Home Page','musician_list':musician_list,'album_list':album_list}
    return render(request, 'adding/index.html',context=diction)

@login_required
def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'title': 'Add Musician','musician_form':form}
    return render(request, 'adding/musician_form.html', context=diction)

@login_required
def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'title': 'Add Album','album_form':form}
    return render(request, 'adding/album_form.html', context=diction)

@login_required
def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_info)
    diction = {'title':'Album List','artist_info':artist_info,'album_list':album_list}
    return render(request, 'adding/album_list.html', context=diction)

@login_required
def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':'Edit Artist Informatiom','artist_form':form}
    return render(request, 'adding/edit_artist.html',context=diction)

@login_required
def edit_album(request,album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction = {}

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction.update({'title':'Edit Album','album_form':form})
    diction.update({'album_id':album_id})
    return render(request, 'adding/edit_album.html', context=diction)

@login_required
def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'title':'Delete Album','delete_massage':'Album Deleted successfully!'}
    return render(request, 'adding/delete.html', context=diction)

@login_required
def delete_artist(request, artist_id):
    artist = Musician.objects.get(pk=artist_id).delete()
    diction = {'title':'Delete Musician','delete_massage':'Musician Deleted successfully!'}
    return render(request, 'adding/delete.html', context=diction)
