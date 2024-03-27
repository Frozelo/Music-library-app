# albums_views.py

from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator

from src.music_app.services.core_service import get_artist_list
from src.scripts.itunes_api_script import save_artist_to_db, fetch_artist_info_from_last_fm, \
    fetch_album_info_from_last_fm, save_album_to_db


# TODO refactor this code, decompose functionality
@method_decorator(csrf_protect, name='dispatch')
class ArtistSearchView(View):
    def get(self, request):
        return render(request, "scripts_templates/artist_search.html")

    def post(self, request):
        artist_name = request.POST.get('artist_name')

        try:
            response_data = fetch_artist_info_from_last_fm(artist_name)
            artist = save_artist_to_db(response_data)
            message = 'Artist saved successfully!'
        except KeyError as e:
            message = f"Missing data in response: {e}"
        except Exception as e:
            message = f"An error occurred: {e}"

        return render(request, "scripts_templates/artist_search.html", {'message': message})


@method_decorator(csrf_protect, name='dispatch')
class AlbumSearchView(View):
    def get(self, request):
        artist_list = get_artist_list()
        return render(request, 'scripts_templates/album_search.html', {'artist_list': artist_list})

    def post(self, request):
        artist_list = get_artist_list()
        artist_name = request.POST.get('artist_name')
        album_name = request.POST.get('album_name')

        try:
            album_data = fetch_album_info_from_last_fm(artist_name, album_name)
            save_album_to_db(album_data)
            message = "Album saved successfully!"
        except KeyError as e:
            message = f"Missing data in response: {e}"
        except Exception as e:
            message = f"An error occurred: {e}"

        return render(request, 'scripts_templates/album_search.html', {'artist_list': artist_list, 'message': message})
