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
        "role",
    ]

    fieldsets = [
        (
            "Basic Info",
            {
                "fields": [
                    "username",
                    "password",
                    "name",
                    "contact",
                    "email",
                    "birthdate",
                ]
            },
        ),
        ("Detail Info", {"fields": ["team", "permission", "position", "role"]}),
    ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "leader"]

    fieldsets = [
        (
            "Basic Info",
            {
                "fields": [
                    "name",
                    "team_image",
                    "leader",
                    "members",
                ]
            },
        )
    ]
