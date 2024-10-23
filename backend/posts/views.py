# Django Libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# Custom Libraries
from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title"]
    search_fields = ["title"]
    ordering_fields = ["title"]
    ordering = ["title"]
