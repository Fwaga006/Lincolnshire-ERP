from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="employees_dashboard"),

    path("employees/", views.employees, name="employees"),
    path("employees/add/", views.add_employee, name="add_employee"),
    path("employees/<int:pk>/edit/", views.edit_employee, name="edit_employee"),
    path("employees/<int:pk>/delete/", views.delete_employee, name="delete_employee"),
]