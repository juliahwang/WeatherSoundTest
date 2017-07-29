from rest_framework import generics, permissions, renderers
from rest_framework.response import Response

from ..models import Snippet
from ..serializers import SnippetSerializer

__all__ = (
    "SnippetList",
    "SnippetHighlight",
)


class SnippetList(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly, # TODO make custom permissions
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
