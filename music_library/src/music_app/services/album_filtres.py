def apply_sorting(albums, sort_by):
    """Применяет сортировку к списку альбомов на основе параметра sort_by."""
    sorting_options = {
        'release_year': 'release_year',
        'title': 'title',
    }

    return albums.order_by(sorting_options.get(sort_by, 'id'))


def apply_filters(request, albums):
    """Применяет фильтры к списку альбомов на основе параметров из запроса."""
    artist_id = request.GET.get('artist')
    sort_by = request.GET.get('sort_by')

    if artist_id:
        albums = albums.filter(artist_id=artist_id)

    if sort_by:
        albums = apply_sorting(albums, sort_by)

    return albums
