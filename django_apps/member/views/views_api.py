from django.contrib.auth import get_user_model
from rest_framework import generics

from ..serializers.user import UserCreationSerializer
from ..serializers.user import UserSerializer

User = get_user_model()

__all__ = (
    "UserListCreateView",
    "UserRetrieveUpdateDestroyView",

)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        elif self.request.method == "POST":
            return UserCreationSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly,
        # ObjectIsRequestUser,
    )
