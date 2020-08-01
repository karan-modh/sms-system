from django.db import models
from django.conf import settings


class Template(models.Model):
    message_type = models.CharField(max_length=40, null=False, blank=False)
    message = models.TextField(help_text="Your Message Template here")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.message_type
