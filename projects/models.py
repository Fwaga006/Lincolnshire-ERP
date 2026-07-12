from django.db import models
from companies.models import Company


class Project(models.Model):

    STATUS = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    project_name = models.CharField(max_length=200)

    customer_name = models.CharField(max_length=200)

    customer_phone = models.CharField(max_length=20)

    location = models.CharField(max_length=200)

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField()

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.project_name