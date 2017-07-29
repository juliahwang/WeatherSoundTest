from django.contrib.auth import get_user_model
from django.db import models

__all__ = (
    'Music',
    'Weather'
)

User = get_user_model()


# 전체 음악파일/정보 모델
class Music(models.Model):
    name_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    img_music = models.ImageField(
        upload_to='img_music',
        blank=True
    )
    name_music = models.CharField(
        max_length=100
    )
    name_singer = models.CharField(
        max_length=100)
    file_music = models.FileField(
        upload_to='music')
    name_album = models.CharField(
        max_length=100,
        blank=True)
    # Need?
    date_created = models.DateTimeField(
        auto_now_add=True)
    sunny = models.PositiveIntegerField(
        verbose_name='맑음',
        default=1
    )
    foggy = models.PositiveIntegerField(
        verbose_name='안개',
        default=1
    )
    rainy = models.PositiveIntegerField(
        verbose_name='비',
        default=1
    )
    cloudy = models.PositiveIntegerField(
        verbose_name='흐림',
        default=1
    )
    snowy = models.PositiveIntegerField(
        verbose_name='눈',
        default=1
    )

    def __str__(self):
        return self.name_music


# 유저별 플레이리스트 모델
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_playlist = models.CharField(max_length=30, default='playlist')
    playlist_musics = models.ManyToManyField(
        'Music',
        through='PlaylistMusics',
        related_name='playlist_musics'
    )

    def __str__(self):
        return '{}의 {}'.format(
            self.user,
            self.name_playlist)


# 유저의 플레이리스트 내 음악 목록 모델
class PlaylistMusics(models.Model):
    name_playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    music = models.ForeignKey('Music', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '리스트 {}의 음악 {}'.format(
            self.name_playlist,
            self.music
        )
