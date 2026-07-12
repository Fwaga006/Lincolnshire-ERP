from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer, Sale, SaleItem
from .forms import CustomerForm, SaleForm, SaleItemForm


# ==========================
# DASHBOARD
# ==========================

def dashboard(request):
    context = {
        "customer_count": Customer.objects.count(),
        "sale_count": Sale.objects.count(),
        "sale_item_count": SaleItem.objects.count(),
        "recent_sales": Sale.objects.order_by("-id")[:10],
    }

    return render(request, "sales/dashboard.html", context)


# ==========================
# CUSTOMERS
# ==========================

def customers(request):
    customers = Customer.objects.all().order_by("name")

    return render(
        request,
        "sales/customers.html",
        {"customers": customers},
    )


def add_customer(request):
    form = CustomerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("customers")

    return render(
        request,
        "sales/customer_form.html",
        {"form": form},
    )


def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    form = CustomerForm(
        request.POST or None,
        instance=customer,
    )

    if form.is_valid():
        form.save()
        return redirect("customers")

    return render(
        request,
        "sales/customer_form.html",
        {"form": form},
    )


def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.delete()
        return redirect("customers")

    return render(
        request,
        "sales/customer_confirm_delete.html",
        {"customer": customer},
    )


# ==========================
# SALES
# ==========================

def sales(request):
    sales = Sale.objects.all().order_by("-id")

    return render(
        request,
        "sales/sales.html",
        {"sales": sales},
    )


def add_sale(request):
    form = SaleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("sales")

    return render(
        request,
        "sales/sale_form.html",
        {"form": form},
    )


def edit_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    form = SaleForm(
        request.POST or None,
        instance=sale,
    )

    if form.is_valid():
        form.save()
        return redirect("sales")

    return render(
        request,
        "sales/sale_form.html",
        {"form": form},
    )


def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    if request.method == "POST":
        sale.delete()
        return redirect("sales")

    return render(
        request,
        "sales/sale_confirm_delete.html",
        {"sale": sale},
    )


def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    return render(
        request,
        "sales/sale_detail.html",
        {"sale": sale},
    )