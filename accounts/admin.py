from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "company",
        "is_platform_admin",
        "is_company_admin",
        "is_staff",
    )

    list_filter = (
        "is_platform_admin",
        "is_company_admin",
        "is_staff",
    )