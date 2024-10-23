# Django Libraries
from rest_framework import serializers

# Custom Libraries
from .models import User, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["created_at"]
        extra_kwargs = {
            # required : 필수 입력 여부
            "role": {"required": False},
        }


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
