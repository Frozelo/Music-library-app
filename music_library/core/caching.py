from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CacheMixin:
    """A base mixin-class for caching"""

    @method_decorator(cache_page(900))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(900))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
