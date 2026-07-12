from django.shortcuts import render
from django.db.models import Sum

from companies.models import Company
from employees.models import Employee
from finance.models import Finance
from inventory.models import Product, Supplier
from sales.models import Customer, Sale
from procurement.models import PurchaseRequisition


def dashboard(request):
    total_income = (
        Finance.objects.filter(transaction_type="Income")
        .aggregate(Sum("amount"))["amount__sum"] or 0
    )

    total_expense = (
        Finance.objects.filter(transaction_type="Expense")
        .aggregate(Sum("amount"))["amount__sum"] or 0
    )

    context = {
        "companies": Company.objects.count(),
        "employees": Employee.objects.count(),
        "products": Product.objects.count(),
        "suppliers": Supplier.objects.count(),
        "customers": Customer.objects.count(),
        "sales": Sale.objects.count(),
        "purchase_requisitions": PurchaseRequisition.objects.count(),
        "income": total_income,
        "expenses": total_expense,
        "profit": total_income - total_expense,
    }

    return render(
        request,
        "business_reports/dashboard.html",
        context,
    )