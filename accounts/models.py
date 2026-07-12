from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    is_platform_admin = models.BooleanField(default=False)
    is_company_admin = models.BooleanField(default=False)

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users"
    )

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
    )

    def _str_(self):
        return self.username