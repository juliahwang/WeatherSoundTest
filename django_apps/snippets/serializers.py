from rest_framework import serializers

# from .models import LANGUAGE_CHOICES, STYLE_CHOICES
from .models import Snippet

__all__ = (
    "SnippetSerializer",

)


class SnippetSerializer(serializers.ModelSerializer):
    owner_info = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight",
        format="html",
    )

    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',

            'owner_info',
            'highlight',
        )

# class SnippetSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False,
#                                   allow_blank=True,
#                                   max_length=100, )
#     code = serializers.CharField(
#         style={
#             "base_template": "textarea.html",
#         },
#     )
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(
#         choices=LANGUAGE_CHOICES,
#         default="python",
#     )
#     style = serializers.ChoiceField(
#         choices=STYLE_CHOICES,
#         default="friendly",
#     )
#
#     def create(self, validated_data):
#         pass
#
#     def update(self, instance, validated_data):
#         pass
