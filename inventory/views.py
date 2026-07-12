from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction

from .models import (
    Product,
    Category,
    Supplier,
    StockTransaction,
    PurchaseOrder,
)

from .forms import (
    ProductForm,
    CategoryForm,
    SupplierForm,
    StockTransactionForm,
    PurchaseOrderForm,
)


# ==========================
# DASHBOARD
# ==========================

def dashboard(request):
    context = {
        "product_count": Product.objects.count(),
        "category_count": Category.objects.count(),
        "supplier_count": Supplier.objects.count(),
        "transaction_count": StockTransaction.objects.count(),
        "products": Product.objects.order_by("-id")[:10],
    }
    return render(request, "inventory/dashboard.html", context)


# ==========================
# PRODUCTS
# ==========================

def products(request):
    products = Product.objects.all().order_by("name")
    return render(request, "inventory/products.html", {
        "products": products
    })


def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("products")

    return render(request, "inventory/product_form.html", {
        "form": form
    })


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    form = ProductForm(
        request.POST or None,
        instance=product
    )

    if form.is_valid():
        form.save()
        return redirect("products")

    return render(request, "inventory/product_form.html", {
        "form": form
    })


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("products")

    return render(request,
                  "inventory/product_confirm_delete.html",
                  {"product": product})


# ==========================
# STOCK TRANSACTIONS
# ==========================

def stock_transactions(request):
    transactions = StockTransaction.objects.select_related(
        "product"
    ).order_by("-created_at")

    return render(request,
                  "inventory/stock_transactions.html",
                  {"transactions": transactions})


@transaction.atomic
def add_stock(request):
    form = StockTransactionForm(request.POST or None)

    if form.is_valid():
        stock = form.save(commit=False)
        stock.transaction_type = StockTransaction.STOCK_IN
        stock.save()

        product = stock.product
        product.quantity += stock.quantity
        product.save()

        return redirect("stock_transactions")

    return render(request,
                  "inventory/stock_form.html",
                  {
                      "form": form,
                      "title": "Stock In"
                  })


@transaction.atomic
def remove_stock(request):
    form = StockTransactionForm(request.POST or None)

    if form.is_valid():
        stock = form.save(commit=False)

        product = stock.product

        if product.quantity >= stock.quantity:
            stock.transaction_type = StockTransaction.STOCK_OUT
            stock.save()

            product.quantity -= stock.quantity
            product.save()

            return redirect("stock_transactions")

    return render(request,
                  "inventory/stock_form.html",
                  {
                      "form": form,
                      "title": "Stock Out"
                  })


# ==========================
# SUPPLIERS
# ==========================

def suppliers(request):
    suppliers = Supplier.objects.all().order_by("name")

    return render(request,
                  "inventory/suppliers.html",
                  {"suppliers": suppliers})


def add_supplier(request):
    form = SupplierForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("suppliers")

    return render(request,
                  "inventory/supplier_form.html",
                  {"form": form})


def edit_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    form = SupplierForm(
        request.POST or None,
        instance=supplier
    )

    if form.is_valid():
        form.save()
        return redirect("suppliers")

    return render(request,
                  "inventory/supplier_form.html",
                  {"form": form})


def delete_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == "POST":
        supplier.delete()
        return redirect("suppliers")

    return render(request,
                  "inventory/supplier_confirm_delete.html",
                  {"supplier": supplier})


# ==========================
# PURCHASE ORDERS
# ==========================

def purchase_orders(request):
    orders = PurchaseOrder.objects.all().order_by("-id")

    return render(
        request,
        "inventory/purchase_orders.html",
        {"orders": orders},
    )


def add_purchase_order(request):
    form = PurchaseOrderForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("purchase_orders")

    return render(
        request,
        "inventory/purchase_order_form.html",
        {"form": form},
    )


def purchase_order_detail(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)

    return render(
        request,
        "inventory/purchase_order_detail.html",
        {"order": order},
    )


def edit_purchase_order(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)

    form = PurchaseOrderForm(
        request.POST or None,
        instance=order,
    )

    if form.is_valid():
        form.save()
        return redirect("purchase_orders")

    return render(
        request,
        "inventory/purchase_order_form.html",
        {"form": form},
    )


def delete_purchase_order(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)

    if request.method == "POST":
        order.delete()
        return redirect("purchase_orders")

    return render(
        request,
        "inventory/purchase_order_confirm_delete.html",
        {"order": order},
    )