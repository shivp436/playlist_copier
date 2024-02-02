from django.shortcuts import redirect, render
from requests import request
from django.http import HttpResponse
from .forms import SourceForm
from .playlist_getters import get_playlists
from .playlist_getters.get_spotify_playlists import callback_spotify

# Create your views here.
def index(request):
    return render(request, 'index.html')

def select_source(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            selected_source = form.cleaned_data['source']
            print(selected_source)
            playlists = get_playlists(request, selected_source)
            print(playlists)
            return redirect('get_playlists:index')

    else:
        form = SourceForm()

    return render(request, 'select_source.html', {'form': form})

def spotify_callback(request):
    print(request)
    return HttpResponse('Callback')