from core.decorators import only_objects_decorator, select_related_objects_decorator, \
    prefetch_related_objects_decorator, objects_exist, order_by_decorator


@select_related_objects_decorator
@prefetch_related_objects_decorator
@only_objects_decorator
@order_by_decorator
def all_objects(obj: callable):
    return obj.all()


@select_related_objects_decorator
@prefetch_related_objects_decorator
def get_objects(obj: callable, **kwargs):
    print(kwargs)
    return obj.get(**kwargs)


@objects_exist
@only_objects_decorator
@select_related_objects_decorator
@prefetch_related_objects_decorator
def filter_objects(obj: callable, **kwargs):
    return obj.filter(**kwargs)
