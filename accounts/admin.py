from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Travel Profile Details', {'fields': ('phone_number', 'passport_number', 'nationality', 'profile_picture', 'email_verified', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Travel Profile Details', {'fields': ('phone_number', 'passport_number', 'nationality', 'profile_picture', 'email_verified', 'bio')}),
    )
    list_display = ['username', 'email', 'phone_number', 'passport_number', 'is_staff']

admin.site.register(User, CustomUserAdmin)
