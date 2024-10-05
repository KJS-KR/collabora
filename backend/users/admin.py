from django.contrib import admin
from .models import User, Team


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username", 
        "name", 
        "email", 
        "team", 
        "permission", 
        "position", 
        "role"
    ]
    
    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "username",
                    "password", 
                    "name",
                    "contact",
                    "email",
                    "birthdate"
                ]
            }
        ),
        (
            "세부정보",
            {
                "fields": [
                    "team",
                    "permission",
                    "position",
                    "role"
                ]
            }
        ),
    ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "name", 
        "leader"
    ]

    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "name",
                    "team_image",
                    "leader",
                    "members",
                ]
            }
        )
    ]
