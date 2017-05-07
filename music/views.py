from django.shortcuts import render
from django.http import Http404
from .models import Albums

# Create your views here.

def index(request):
    all_albums = Albums.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

def details(request, album_id):
    try:
        album = Albums.objects.get(pk=album_id)
    except Albums.DoesNotExist:
        raise Http404('Album Doesnot exit')
    return render(request, 'music/detail.html', {'album':album})

