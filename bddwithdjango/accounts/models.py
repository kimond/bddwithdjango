from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Interest(models.Model):
    name = models.CharField(max_length=255)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    interests = models.ManyToManyField(Interest)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass
