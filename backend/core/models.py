# Django Libraries
from django.utils.timezone import now, timedelta
from django.db import models

# Custom Libraries


# Python Libraries


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="삭제일")

    class Meta:
        abstract = True


class JsonWebToken(TimeStampedModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="jwt_token",
        verbose_name="사용자",
    )
    access_token = models.CharField(
        max_length=255,
        verbose_name="액세스 토큰",
    )
    access_expires_at = models.DateTimeField(
        verbose_name="액세스 토큰 만료일",
    )
    refresh_token = models.CharField(
        max_length=255,
        verbose_name="리프레시 토큰",
    )
    refresh_expires_at = models.DateTimeField(
        verbose_name="리프레시 토큰 만료일",
    )

    class Meta:
        verbose_name = "JWT 토큰"
        verbose_name_plural = "JWT 토큰"

    def __str__(self):
        return f"{self.id} - {self.user.username}"
