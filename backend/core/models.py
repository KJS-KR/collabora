from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="변경일")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="삭제일")
    
    class Meta:
        abstract = True