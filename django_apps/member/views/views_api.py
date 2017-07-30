from django.contrib.auth import get_user_model
from rest_framework import generics

<<<<<<< HEAD
from ..serializers.user import UserSerializer, UserCreationSerializer
=======
from ..serializers.user import UserSerializer
>>>>>>> 5e21bf9c246b6a3e86a3f587d420a114c4936b18

User = get_user_model()

__all__ = (
    "UserListCreateView",
<<<<<<< HEAD
    "UserRetrieveUpdateDestroyView",
=======
>>>>>>> 5e21bf9c246b6a3e86a3f587d420a114c4936b18

)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
<<<<<<< HEAD

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        elif self.request.method == "POST":
            return UserCreationSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (
    #
    # )
=======
>>>>>>> 5e21bf9c246b6a3e86a3f587d420a114c4936b18
