from django.db import models
from django.contrib.auth.models import User as auth_user


class User(models.Model):
    phone_no = models.CharField(max_length=10)
    user = models.OneToOneField(auth_user, on_delete=models.CASCADE, related_name='phone_no')

    def __str__(self):
        return self.user
