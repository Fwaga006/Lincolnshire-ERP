from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path("", views.dashboard, name="sales_dashboard"),

    # Customers
    path("customers/", views.customers, name="customers"),
    path("customers/add/", views.add_customer, name="add_customer"),
    path("customers/<int:pk>/edit/", views.edit_customer, name="edit_customer"),
    path("customers/<int:pk>/delete/", views.delete_customer, name="delete_customer"),

    # Sales
    path("sales/", views.sales, name="sales"),
    path("sales/add/", views.add_sale, name="add_sale"),
    path("sales/<int:pk>/", views.sale_detail, name="sale_detail"),
    path("sales/<int:pk>/edit/", views.edit_sale, name="edit_sale"),
    path("sales/<int:pk>/delete/", views.delete_sale, name="delete_sale"),
]