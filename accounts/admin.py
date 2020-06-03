from django.contrib import admin
from .models import UserProfile, User


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile
        fields = '__all__'
