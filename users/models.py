from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_avatar(instance, filename):
    return f'profile/{instance.username}/{filename}'


class User(AbstractUser):
    profile_image = models.ImageField(upload_to=profile_avatar, default='profile/default.png')

    def __str__(self):
        return self.username
