# Generated by Django 4.2.11 on 2024-03-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0005_alter_album_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
