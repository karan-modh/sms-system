from django.db import models
from django.contrib.auth.models import User
import random
from django.conf import settings
from django.template.loader import render_to_string
from django.apps import apps


# User Models defined here ...
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name(), self.company