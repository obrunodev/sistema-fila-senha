from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from apps.users.models import User
from django.contrib.auth.models import Group

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = [
        (
            'Basic Information', {
                'fields': ['username', 'password', 'first_name', 'last_name', 'email', 'profile_picture']
            },
        ),
        (
            'Permissions', {
                'fields': ['is_superuser', 'is_staff']
            }
        )
    ]
    
    list_display = ("username", "email", "full_name", )
    list_filter = ("is_superuser", "is_active")
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = _("Full Name")


admin.site.unregister(Group)
