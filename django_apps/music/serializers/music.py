from rest_framework import serializers

from ..models import Music

__all__ = (
    "MusicSerializer",

)

# TODO update가 필요한가??

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = (
            "pk",
            "name_author",
            "name_music",
            "name_singer",
            "file_music",
            "name_album",
            "date_created",
            "sunny",
            "foggy",
            "rainy",
            "cloudy",
            "snowy"
        )
