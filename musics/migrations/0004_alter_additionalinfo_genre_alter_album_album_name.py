# Generated by Django 4.1.7 on 2023-02-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_alter_additionalinfo_genre_alter_album_album_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Blues'), (2, 'Rock'), (8, 'Disco'), (9, 'Electronic'), (7, 'Folk'), (12, 'Pop'), (1, 'Hip hop'), (11, 'Classical'), (3, 'Rhythm and blues'), (4, 'Soul'), (6, 'Funk'), (5, 'Country'), (0, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
