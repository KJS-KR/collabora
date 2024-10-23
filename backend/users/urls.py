# Django Libraries
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Custom Libraries
from .views import *

# routing 설정
# REST API URL을 자동으로 생성
router = DefaultRouter()
router.register("user", UserViewSet)
router.register("team", TeamViewSet)


urlpatterns = [
    # name : Django Template에서 사용하는 이름
    # 클라이언트가 다른 프레임워크 시엔 사용하지 않음
    path("create_team/", create_team, name="create_team"),
    path("api/", include(router.urls)),
]
