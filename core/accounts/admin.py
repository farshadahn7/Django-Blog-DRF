from django.contrib import admin

from .models import Profile, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser', 'is_verified']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','first_name', 'last_name']