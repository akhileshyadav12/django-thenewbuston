from django.shortcuts import render, get_object_or_404
from .models import Albums, Songs
import pdb


# Create your views here.

def index(request):
    all_albums = Albums.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

def details(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    return render(request, 'music/detail.html', {'album':album})

def favourite(request, album_id):
    #print(album_id)
    album = get_object_or_404(Albums, pk=album_id)
    #request = request.POST['song']
    try:
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except (KeyError, Songs.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album':album,
            'error_message':'You did not select a valid song',
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

