from django.contrib import admin

from .models import (
    PurchaseRequisition,
    PurchaseRequisitionItem,
    SupplierQuotation,
    GoodsReceivedNote,
)


@admin.register(PurchaseRequisition)
class PurchaseRequisitionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "department",
        "requested_by",
        "status",
        "request_date",
    )
    list_filter = (
        "status",
        "request_date",
    )
    search_fields = (
        "department",
        "requested_by",
    )


@admin.register(PurchaseRequisitionItem)
class PurchaseRequisitionItemAdmin(admin.ModelAdmin):
    list_display = (
        "requisition",
        "product",
        "quantity",
    )


@admin.register(SupplierQuotation)
class SupplierQuotationAdmin(admin.ModelAdmin):
    list_display = (
        "supplier",
        "reference",
        "quotation_date",
    )
    list_filter = (
        "quotation_date",
    )


@admin.register(GoodsReceivedNote)
class GoodsReceivedNoteAdmin(admin.ModelAdmin):
    list_display = (
        "supplier",
        "reference",
        "received_date",
    )
    list_filter = (
        "received_date",
    )