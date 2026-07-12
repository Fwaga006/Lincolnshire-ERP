from django.db import models

from inventory.models import Product, Supplier


class PurchaseRequisition(models.Model):
    department = models.CharField(max_length=100)

    requested_by = models.CharField(max_length=100)

    request_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    remarks = models.TextField(blank=True)

    def _str_(self):
        return f"PR-{self.id}"


class PurchaseRequisitionItem(models.Model):
    requisition = models.ForeignKey(
        PurchaseRequisition,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    def _str_(self):
        return self.product.name


class SupplierQuotation(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    quotation_date = models.DateField()

    reference = models.CharField(max_length=100)

    def _str_(self):
        return self.reference


class GoodsReceivedNote(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    received_date = models.DateField(auto_now_add=True)

    reference = models.CharField(max_length=100)

    def _str_(self):
        return self.reference