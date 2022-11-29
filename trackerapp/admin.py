from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Project
from .forms import *
"""
We also need to register our custom user model with the admin
Tell the admin to use these forms by subclassing UserAdmin.

"""

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email','username', 'is_staff', 'is_active',)
    list_filter = ('email','username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Project)

