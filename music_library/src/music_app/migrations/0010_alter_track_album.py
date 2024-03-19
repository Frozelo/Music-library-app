# Generated by Django 4.2.11 on 2024-03-19 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0009_remove_album_tracks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='music_app.album'),
        ),
    ]