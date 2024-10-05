from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", 
        "author", 
        "views", 
        "likes",
    ]
    
    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "title",
                    "content",
                    "author",
                    "views",
                    "likes",
                    "status"
                ]
            }
        ),
    ]