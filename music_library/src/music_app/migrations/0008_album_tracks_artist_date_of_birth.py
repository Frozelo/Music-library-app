# Generated by Django 4.2.11 on 2024-03-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0007_artist_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(blank=True, related_name='albums', to='music_app.track'),
        ),
        migrations.AddField(
            model_name='artist',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]