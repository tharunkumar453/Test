from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
class CustomUserModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True,blank=False)
    phone = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

