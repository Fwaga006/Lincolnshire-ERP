from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    quantity = models.PositiveIntegerField(default=0)

    unit_price = models.DecimalField(max_digits=12, decimal_places=2)

    reorder_level = models.PositiveIntegerField(default=10)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def stock_value(self):
        return self.quantity * self.unit_price

    @property
    def low_stock(self):
        return self.quantity <= self.reorder_level

    def __str__(self):
        return self.name


class StockTransaction(models.Model):

    STOCK_IN = "IN"
    STOCK_OUT = "OUT"

    TRANSACTION_TYPES = [
        (STOCK_IN, "Stock In"),
        (STOCK_OUT, "Stock Out"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    transaction_type = models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPES
    )

    quantity = models.PositiveIntegerField()

    reference = models.CharField(max_length=100, blank=True)

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.transaction_type} ({self.quantity})"


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    order_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"PO-{self.id}"


class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product.name}"