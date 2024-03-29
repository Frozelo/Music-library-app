from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response


def get_cache_key(cache_prefix_key, pk=None):
    """
    Generate a unique cache key for a view
    """
    if pk:
        return f'{cache_prefix_key}_detail_{pk}'
    return f'{cache_prefix_key}_list'


def cached_response(cache_key, view_method, request, cache_timeout, *args, **kwargs):
    """
    Get or set cached response for the given cache key.
    """
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return Response(cached_data, status=status.HTTP_200_OK)

    response = view_method(request, *args, **kwargs)
    cache.set(cache_key, response.data, cache_timeout)
    return response


class CacheMixin:
    """
    A base mixin-class for caching, which uses cache_page decorator
    on the list and retrieve methods.
    """
    cache_timeout = 900
    cache_prefix_key = None

    def list(self, request, *args, **kwargs):
        cache_key = get_cache_key(cache_prefix_key=self.cache_prefix_key)
        return cached_response(cache_key, super().list, request, self.cache_timeout, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cache_key = get_cache_key(cache_prefix_key=self.cache_prefix_key, pk=pk)
        return cached_response(cache_key, super().retrieve, request, self.cache_timeout, *args, **kwargs)
