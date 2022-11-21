from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Project
from .forms import *
"""
We also need to register our custom user model with the admin
Tell the admin to use these forms by subclassing UserAdmin.

"""


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project)

