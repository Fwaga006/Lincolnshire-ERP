from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="procurement_dashboard"),

    path(
        "purchase-requisitions/",
        views.purchase_requisitions,
        name="purchase_requisitions",
    ),
    path(
        "purchase-requisitions/add/",
        views.add_purchase_requisition,
        name="add_purchase_requisition",
    ),
    path(
        "purchase-requisitions/<int:pk>/edit/",
        views.edit_purchase_requisition,
        name="edit_purchase_requisition",
    ),
    path(
        "purchase-requisitions/<int:pk>/delete/",
        views.delete_purchase_requisition,
        name="delete_purchase_requisition",
    ),

    path(
        "supplier-quotations/",
        views.supplier_quotations,
        name="supplier_quotations",
    ),
    path(
        "supplier-quotations/add/",
        views.add_supplier_quotation,
        name="add_supplier_quotation",
    ),

    path(
        "goods-received-notes/",
        views.goods_received_notes,
        name="goods_received_notes",
    ),
    path(
        "goods-received-notes/add/",
        views.add_goods_received_note,
        name="add_goods_received_note",
    ),
]