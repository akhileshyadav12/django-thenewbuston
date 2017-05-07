from django.shortcuts import render
from django.http import HttpResponse
from .models import Albums

# Create your views here.

def index(request):
    all_albums = Albums.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

def details(request, album_id):
    return HttpResponse('<h2>Details for Album ID: ' + str(album_id) + '</h2>')

