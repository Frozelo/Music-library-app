from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging

from src.music_app.models import Album

logging.basicConfig(filename='cache_info.log', level=logging.INFO)
cache_logger = logging.getLogger('cache_test')


@receiver(post_save, sender=Album)
@receiver(post_delete, sender=Album)
def clear_album_list_cache(sender, instance, **kwargs):

    cache_logger.info('clear_album_list_cache')
    if kwargs.get('created', False) or 'created' not in kwargs:
        cache.clear()
