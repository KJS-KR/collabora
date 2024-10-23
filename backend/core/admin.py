from django.contrib import admin
from .models import JsonWebToken


@admin.register(JsonWebToken)
class JsonWebTokenAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "access_expires_at",
        "refresh_expires_at",
    ]

    fieldsets = [
        (
            "Basic Info",
            {
                "fields": [
                    "user",
                    "access_token",
                    "access_expires_at",
                    "refresh_token",
                    "refresh_expires_at",
                ]
            },
        )
    ]
