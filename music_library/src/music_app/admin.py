from django.contrib import admin

from .models import Artist, Album, Track, Genre, AlbumUserRelationship


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'genre')
    list_filter = ('genre',)
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'artist')
    list_filter = ('release_year',)
    search_fields = ('title', 'artist__name')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'display_artists', 'album')
    list_filter = ('album__artist', 'album__release_year')
    search_fields = ('title', 'artist__name', 'album__title')

    def display_artists(self, obj):
        return ', '.join([artist.name for artist in obj.artist.all()])

    display_artists.short_description = 'Artists'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(AlbumUserRelationship)
class AlbumUserRelationshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'album', 'created_at')
    list_filter = ('album__artist', 'album__release_year')
    search_fields = ('user__username', 'album__title')