from django.contrib import admin

from core import models
from utils.admin import TimeStampedModelAdminMixin


@admin.register(models.UserProfile)
class UserProfileAdmin(TimeStampedModelAdminMixin, admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'steam_nickname',
        'discord_nickname'
    )
    search_fields = (
        'email',
        'name',
        'steam_nickname',
        'discord_nickname'
    )
