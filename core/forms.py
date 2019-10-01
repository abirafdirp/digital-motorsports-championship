from django import forms

from core import models


class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = (
            'email',
            'name',
            'steam_nickname',
            'discord_nickname'
        )
