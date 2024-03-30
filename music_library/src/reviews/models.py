from django.conf import settings
from django.db import models

from src.music_app.models import Album

RATING_CHOICES = [
    (1, 'Very Poor'),
    (2, 'Poor'),
    (3, 'Average'),
    (4, 'Good'),
    (5, 'Excellent'),
]


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='album_reviews'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.album.title}"

    class Meta:
        unique_together = ('user', 'album')
        ordering = ['-created_at']
