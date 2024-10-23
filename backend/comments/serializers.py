# Django Libraries
from rest_framework import serializers

# Custom Libraries
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
