from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="companies_dashboard"),

    path("companies/", views.companies, name="companies"),
    path("companies/add/", views.add_company, name="add_company"),
    path("companies/<int:pk>/edit/", views.edit_company, name="edit_company"),
    path("companies/<int:pk>/delete/", views.delete_company, name="delete_company"),
]