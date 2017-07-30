from rest_framework import serializers

from ..models import Playlist

__all__ = (
    "PlaylistSerializer",

)


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = (
            "pk",
            "user",
            # TODO 음악 list가 나오도록
            "playlist_musics",

        )
