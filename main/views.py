from django.shortcuts import render

from companies.models import Company
from employees.models import Employee
from finance.models import Finance
from inventory.models import Product, Supplier
from procurement.models import PurchaseRequisition
from sales.models import Customer, Sale


def home(request):
    context = {
        "company_count": Company.objects.count(),
        "employee_count": Employee.objects.count(),
        "finance_count": Finance.objects.count(),
        "product_count": Product.objects.count(),
        "supplier_count": Supplier.objects.count(),
        "customer_count": Customer.objects.count(),
        "sale_count": Sale.objects.count(),
        "requisition_count": PurchaseRequisition.objects.count(),
    }

    return render(request, "main/home.html", context)