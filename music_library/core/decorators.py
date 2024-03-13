def select_related_objects_decorator(func):
    def wrapper(obj, select_related=(), *args, **kwargs):
        return func(obj, *args, **kwargs).select_related(*select_related)

    return wrapper


def prefetch_related_objects_decorator(func):
    def wrapper(obj, prefetch_related=(), *args, **kwargs):
        return func(obj, *args, **kwargs).prefetch_related(*prefetch_related)

    return wrapper


def only_objects_decorator(func):
    def wrapper(obj, only=(), *args, **kwargs):
        return func(obj, *args, **kwargs).only(*only)

    return wrapper


def objects_exist(func):
    def wrapper(obj, exist=False, *args, **kwargs):
        queryset = func(obj, *args, **kwargs)
        if exist:
            return queryset.exists()
        return queryset

    return wrapper
