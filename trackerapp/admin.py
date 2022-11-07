from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
"""
We also need to register our custom user model with the admin
Tell the admin to use these forms by subclassing UserAdmin.

"""

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)