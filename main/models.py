from django.db import models
from django.conf import settings


class FileUpload(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name


class MessageManager(models.Manager):
    def create_message(self, message, contacts, user):
        msgObj = self.create(message=message, contacts=contacts, author=user)
        return msgObj


class MessagesGenerated(models.Model):
    message = models.TextField(verbose_name='Message')
    contacts = models.TextField(verbose_name='Send To')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = MessageManager()

    def __str__(self):
        return self.author.first_name + ' ' + self.author.last_name + ' ------- ' + self.message