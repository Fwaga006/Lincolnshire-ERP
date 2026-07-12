from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path("", views.dashboard, name="inventory_dashboard"),

    # Products
    path("products/", views.products, name="products"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/<int:pk>/edit/", views.edit_product, name="edit_product"),
    path("products/<int:pk>/delete/", views.delete_product, name="delete_product"),

    # Suppliers
    path("suppliers/", views.suppliers, name="suppliers"),
    path("suppliers/add/", views.add_supplier, name="add_supplier"),
    path("suppliers/<int:pk>/edit/", views.edit_supplier, name="edit_supplier"),
    path("suppliers/<int:pk>/delete/", views.delete_supplier, name="delete_supplier"),

    # Stock Transactions
    path("transactions/", views.stock_transactions, name="stock_transactions"),
    path("stock-in/", views.add_stock, name="add_stock"),
    path("stock-out/", views.remove_stock, name="remove_stock"),

    # Purchase Orders
    path("purchase-orders/", views.purchase_orders, name="purchase_orders"),
    path("purchase-orders/add/", views.add_purchase_order, name="add_purchase_order"),
    path("purchase-orders/<int:pk>/", views.purchase_order_detail, name="purchase_order_detail"),
    path("purchase-orders/<int:pk>/edit/", views.edit_purchase_order, name="edit_purchase_order"),
    path("purchase-orders/<int:pk>/delete/", views.delete_purchase_order, name="delete_purchase_order"),
]