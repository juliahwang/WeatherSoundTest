from django.contrib.auth import get_user_model
from rest_framework import generics

from ..serializers.user import UserSerializer

User = get_user_model()

__all__ = (
    "UserListCreateView",

)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
