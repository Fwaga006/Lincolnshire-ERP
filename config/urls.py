from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("main.urls")),

    path("companies/", include("companies.urls")),
    path("employees/", include("employees.urls")),
    path("finance/", include("finance.urls")),

    path("inventory/", include("inventory.urls")),
    path("procurement/", include("procurement.urls")),

   path("sales/", include("sales.urls")),

   path("business-reports/", include("business_reports.urls")),
]