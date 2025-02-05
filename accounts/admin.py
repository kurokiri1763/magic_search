from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('account_id', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('account_id',)

    fieldsets = (
        (None, {'fields': ('account_id', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'birth_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account_id', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(User, CustomUserAdmin)
