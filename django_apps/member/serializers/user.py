from django.contrib.auth import get_user_model
# from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

User = get_user_model()

__all__ = (
    "UserSerializer",
    "UserUpdateSerializer",
    "UserCreationSerializer",

)


# TODO Password fiedls?
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "username",
            "img_profile",

        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "username",
            "ori_password",
            "password01",
            "password02",
            "img_profile",

        )
        read_only_fields = (
            "email",
        )


# TODO img_profile처리
class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "username",
            "password",
            "img_profile",
        )

    # password = serializers.CharField(_('password'), max_length=128)

    def validated_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already Exists")
        return email

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already Exists")
        return username

    # def validate(self, attrs):
    #     if attrs["password01"] != attrs["password02"]:
    #         raise serializers.ValidationError('Passwords didn\'t match')
    #     return attrs

    def create(self, validated_data):
        email = self.validated_data.get("email", "")
        username = self.validated_data.get("username", "")
        password = self.validated_data.get("password02", "")
        img_profile = self.validated_data.get("img_profile", "")
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            img_profile=img_profile,
        )
        return user
