# Django Libraries
from rest_framework import serializers

# Custom Libraries
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
