from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_platform_admin = models.BooleanField(default=False)
    is_company_admin = models.BooleanField(default=False)

    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='users'
    )

    def _str_(self):
        return self.username