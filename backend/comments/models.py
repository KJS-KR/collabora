# Django Libraries
from django.db import models

# Custom Libraries
from core.models import TimeStampedModel


class Comment(TimeStampedModel):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="작성자")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, verbose_name="게시글")
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, verbose_name="상위 댓글")
    content = models.TextField(verbose_name="내용")
    likes = models.IntegerField(default=0, verbose_name="좋아요 수")
    dislikes = models.IntegerField(default=0, verbose_name="싫어요 수")
    status = models.CharField(max_length=50, default="active", verbose_name="상태")
    
    class Meta:
        db_table = "comments"
        ordering = ["-created_at"]
        verbose_name = "댓글"
        verbose_name_plural = "댓글"    
        
    # 작성자, 게시글
    def __str__(self):
        return f"{self.author} - {self.post}"