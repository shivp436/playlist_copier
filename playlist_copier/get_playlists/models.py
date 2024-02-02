from django.db import models

# Create your models here.
class Source(models.Model):
    SPOTIFY = 'spotify'
    YOUTUBE = 'youtube'

    SOURCE_CHOICES = [
        (SPOTIFY, 'Spotify'),
        (YOUTUBE, 'YouTube'),
    ]

    source = models.CharField(max_length=10, choices=SOURCE_CHOICES)