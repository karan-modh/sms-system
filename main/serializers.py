from rest_framework import serializers
from .models import FileUpload, MessagesGenerated


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesGenerated
        fields = "__all__"
