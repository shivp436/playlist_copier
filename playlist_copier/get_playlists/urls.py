from django.urls import path
from . import views

app_name = 'get_playlists'

urlpatterns = [
    path('', views.index, name='index'),
    path('select_source', views.select_source, name='select_source'),
    path('callback', views.spotify_callback, name='spotify_callback')
]