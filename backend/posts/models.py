# Django Libraries
from django.db import models

# Custom Libraries
from core.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=50, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="작성자")
    # category = 
    views = models.IntegerField(default=0, verbose_name="조회수")
    likes = models.IntegerField(default=0, verbose_name="좋아요 수")
    # draft, published, deleted
    status = models.CharField(max_length=50, default="draft", verbose_name="상태")
    
    
    class Meta:
        db_table = "posts"
        ordering = ["-created_at"]
        verbose_name = "게시글"
        verbose_name_plural = "게시글"
    
    def __str__(self):
        return f"{self.author} - {self.title}"