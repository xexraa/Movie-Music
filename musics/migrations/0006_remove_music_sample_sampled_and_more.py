# Generated by Django 4.1.7 on 2023-02-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0005_music_sample_sampled_alter_additionalinfo_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='sample_sampled',
        ),
        migrations.AlterField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(6, 'Funk'), (8, 'Disco'), (10, 'Blues'), (12, 'Pop'), (0, 'Other'), (5, 'Country'), (4, 'Soul'), (9, 'Electronic'), (1, 'Hip hop'), (7, 'Folk'), (3, 'Rhythm and blues'), (11, 'Classical'), (2, 'Rock')], default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
