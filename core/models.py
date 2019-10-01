from django.db import models

from utils.models import TimeStampedModel


class UserProfile(TimeStampedModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    steam_nickname = models.CharField(max_length=255)
    discord_nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.email
