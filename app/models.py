from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core import validators

class User(AbstractUser):
    email = models.EmailField(max_length=30, unique=True, validators=[validators.EmailValidator(message="Invalid Email")])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Todo(models.Model):
    task = models.CharField(max_length=20, blank=False)
    date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.task
