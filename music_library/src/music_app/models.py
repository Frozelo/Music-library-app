from django.conf import settings
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now_add=False, blank=True, null=True)
    country = models.CharField(max_length=50)
    biography = models.TextField()
    avatar_image = models.URLField(max_length=200, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    itunes_id = models.IntegerField(unique=True, null=True, blank=True)


    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    biography = models.TextField(blank=True, null=True)
    cover_image = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class AlbumUserRelationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'album')


class Track(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField(blank=True, null=True)
    artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks', blank=True, null=True)
    audio_file = models.FileField(upload_to='media/tracks/songs/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='media/tracks/covers/', blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {", ".join([artist.name for artist in self.artist.all()])}: {self.duration}'


class TrackUserRelationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'track')
