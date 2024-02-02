from .get_spotify_playlists import get_spotify_playlists


def get_playlists(request, source):
    if source == 'spotify':
        playlists = get_spotify_playlists(request)
        return playlists
    else:
        return 'No functions found'