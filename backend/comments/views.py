# Django Libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# Custom Libraries
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
