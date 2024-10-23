# Django Libraries
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# Custom Libraries
from .serializers import UserSerializer, TeamSerializer
from .models import User, Team


@api_view(["POST"])
def create_team(request):
    serializer = TeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]

    # detail : True -> URL에 id가 포함되어야 함
    @action(detail=True, methods=["POST"])
    def activate(self, request, pk=None):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({"msg": "활성화 성공"}, status=200)

    @action(detail=True, methods=["POST"])
    def deactivate(self, request, pk=None):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({"msg": "비활성화 성공"}, status=200)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["name"]
