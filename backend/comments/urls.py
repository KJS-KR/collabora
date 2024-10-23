# Django Libraries
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Custom Libraries
from .views import *

router = DefaultRouter()
router.register("comment", CommentViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
