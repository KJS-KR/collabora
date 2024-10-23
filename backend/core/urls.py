# Django Libraries
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Custom Libraries
from .views import *

urlpatterns = [
    path("auth/login", login),
]
