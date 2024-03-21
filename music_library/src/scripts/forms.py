from django import forms


class ArtistSearchForm(forms.Form):
    artist_name = forms.CharField(label='Введите имя артиста', max_length=100)
