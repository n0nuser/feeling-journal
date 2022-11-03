from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(("email address"), unique=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Users"
