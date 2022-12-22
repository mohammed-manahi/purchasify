from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Register customized user in admin site
    """
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                # Add email, first name and last name fields to default fields
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
