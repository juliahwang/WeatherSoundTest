from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

# User = get_user_model()

__all__ = (
    "Music",
    "MusicList",
    "SongList",

)

User = get_user_model()


# 맑음 흐림 비 눈 안개
class Music(models.Model):
    # WEATHERS = (
    #     ("sunny", "맑음"),
    #     ("cloudy", "흐림"),
    #     ("rainy", "비"),
    #     ("snowy", "눈"),
    #     ("foggy", "안개"),
    # )
    name_music = models.CharField(
        max_length=100
    )
    name_singer = models.CharField(
        max_length=100
    )
    name_album = models.CharField(
        max_length=100,
        null=True
    )
    img_music = models.ImageField(
        upload_to='img_music',
        blank=True,
        null=True,
    )
    file_music = models.FileField(
        # upload_to='music'
        null=True,
    )

    sunny = models.PositiveIntegerField(
        verbose_name='맑음', default=1)
    foggy = models.PositiveIntegerField(
        verbose_name='안개', default=1)
    rainy = models.PositiveIntegerField(
        verbose_name='비', default=1)
    cloudy = models.PositiveIntegerField(
        verbose_name='흐림', default=1)
    snowy = models.PositiveIntegerField(
        verbose_name='눈', default=1)

    def __str__(self):
        return "name : {}\nartist : {}".format(self.name_music, self.name_singer)


class MusicList(models.Model):
    name = models.CharField(
        max_length=30,
        null=True,
    )
    user = models.ForeignKey(User)


class SongList(models.Model):
    play_list = models.ForeignKey(MusicList)
    songs = models.ManyToManyField(
        "Music",
        related_name="song_list",
    )
