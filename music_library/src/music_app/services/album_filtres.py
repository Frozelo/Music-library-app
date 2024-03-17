def apply_sorting(albums, sort_by):
    """Применяет сортировку к списку альбомов на основе параметра sort_by."""
    sorting_options = {
        'release_year': 'release_year',
        'title': 'title',
    }

    return albums.order_by(sorting_options.get(sort_by, 'id'))


FILTER_ACTIONS = {
    'artist': lambda queryset, value: queryset.filter(artist_id=value),
    'genre': lambda queryset, value: queryset.filter(genre_id=value),
    'sort_by': apply_sorting,
}


def apply_filters(request, queryset):
    """Применяет фильтры к queryset на основе параметров из запроса."""
    filters = {
        'artist': request.GET.get('artist'),
        'genre': request.GET.get('genre'),
        'sort_by': request.GET.get('sort_by'),
    }

    filtered_queryset = queryset

    for key, value in filters.items():
        if value:
            filtered_queryset = FILTER_ACTIONS[key](filtered_queryset, value)

    return filtered_queryset
