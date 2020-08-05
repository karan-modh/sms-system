from django.contrib import admin
from .models import FileUpload
from .models import MessagesGenerated

# Register your models here.
admin.site.register(FileUpload)
admin.site.register(MessagesGenerated)