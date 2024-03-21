from django.shortcuts import render
from .forms import ArtistSearchForm
from .itunes_api_script import fetch_and_save_artist_info, save_artist_albums


def artist_search_view(request):
    if request.method == 'POST':
        form = ArtistSearchForm(request.POST)
        if form.is_valid():
            artist_name = form.cleaned_data['artist_name']
            artist = fetch_and_save_artist_info(artist_name)
            if artist:
                return render(request, 'scripts_templates/artist_details.html', {'artist': artist})
            else:
                return render(request, 'scripts_templates/artist_not_found.html')
    else:
        form = ArtistSearchForm()

    return render(request, 'scripts_templates/artist_search.html', {'form': form})


def save_artist_albums_view(request, artist_id):
    save_artist_albums(artist_id)
