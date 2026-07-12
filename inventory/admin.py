from django.contrib import admin
from .models import (
    Category,
    Supplier,
    Product,
    StockTransaction,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
    )
    search_fields = (
        "name",
        "email",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "supplier",
        "quantity",
        "unit_price",
        "reorder_level",
        "is_active",
    )

    list_filter = (
        "category",
        "supplier",
        "is_active",
    )

    search_fields = (
        "name",
        "sku",
    )


@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "transaction_type",
        "quantity",
        "reference",
        "created_at",
    )

    list_filter = (
        "transaction_type",
    )

    search_fields = (
        "product__name",
        "reference",
    )