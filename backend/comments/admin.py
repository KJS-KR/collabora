from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "author", 
        "post",
    ]
    
    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "author",
                    "post",
                    "parent_comment",
                    "content",
                    "likes",
                    "dislikes",
                    "status"
                ],
            },
        ),
    ]