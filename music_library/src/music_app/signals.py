from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging

from src.music_app.models import Album, Artist

logging.basicConfig(filename='cache_info.log', level=logging.INFO)
cache_logger = logging.getLogger('cache_test')


# TODO: Work with cache invalidation
@receiver(post_save, sender=[])
@receiver(post_delete, sender=Artist)
def clear_artist_detail_cache(sender, instance, **kwargs):
    cache.clear()


@receiver(post_save, sender=Album)
@receiver(post_delete, sender=Album)
def clear_related_artist_and_albums_list_cache(sender, instance, **kwargs):
    cache.clear()
