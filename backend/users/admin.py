from django.contrib import admin
from .models import User, Team


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ["name", "is_active"]

    list_display = [
        "username",
        "name",
        "email",
        "team",
        "permission",
        "position",
        "role",
    ]

    search_fields = ["username", "name", "email"]

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
        (
            "Detail Info",
            {
                "fields": [
                    "team",
                    "permission",
                    "position",
                    "role",
                    "is_active",
                ]
            },
        ),
    ]

    actions = ["activate_users", "deactivate_users"]

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "선택된 사용자 을/를 활성화합니다."

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_users.short_description = "선택된 사용자 을/를 비활성화합니다."


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "leader"]

    search_fields = ["name"]

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
