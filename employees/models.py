from django.db import models
from companies.models import Company


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    job_title = models.CharField(max_length=100)

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    photo = models.ImageField(
        upload_to="employees/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"