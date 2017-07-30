# Create your views here.
from rest_framework import generics

from music.serializers.playList import PlaylistSerializer
from ..models import Music, Playlist
from ..serializers.music import MusicSerializer

__all__ = (
    "MusicListCreateView",
    "MusicRetrieveView",
    "PlaylistListCreateView",
)


# TODO create, update, delete 넣어야 하나?
class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicRetrieveView(generics.RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
