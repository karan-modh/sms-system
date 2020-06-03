from django.db import models


# Create your models here.
class MessageTemplate(models.Model):
    # Choices
    TYPE = (
        ('1', 'Discount'),
        ('2', 'Data Usage Notification')
    )
    template_type = models.CharField(max_length=1, choices=TYPE)
    data_msg = models.TextField()

    def getTypeName(self):
        return self.TYPE[int(self.template_type)-1][1]

    def __str__(self):
        return self.getTypeName()