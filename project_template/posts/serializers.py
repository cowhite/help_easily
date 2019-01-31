from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post


class PostContentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'content', 'post_type', 'user')

