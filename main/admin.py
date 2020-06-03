from django.contrib import admin
from .models import MessageTemplate


# Register your models here.
@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    class Meta:
        model = MessageTemplate
        fields = '__all__'
