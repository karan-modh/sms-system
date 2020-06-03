from django.db import models
from django.contrib.auth.models import User


# User Models defined here ...
class UserProfile(models.Model):
    # Choices
    POST_CHOICES = (
        ('O', 'Owner'),
        ('M', 'Manager'),
        ('P', 'Public-Relations')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=1, choices=POST_CHOICES, default='P')

    def __str__(self):
        return self.user.get_full_name() + " | " + self.company