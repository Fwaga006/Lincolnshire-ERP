from django.shortcuts import render, redirect, get_object_or_404

from .models import Finance
from .forms import FinanceForm


# ==========================
# DASHBOARD
# ==========================

def dashboard(request):
    context = {
        "transaction_count": Finance.objects.count(),
        "transactions": Finance.objects.order_by("-id")[:10],
    }

    return render(request, "finance/dashboard.html", context)


# ==========================
# TRANSACTIONS
# ==========================

def transactions(request):
    transactions = Finance.objects.all().order_by("-transaction_date")

    return render(
        request,
        "finance/transactions.html",
        {"transactions": transactions},
    )


def add_transaction(request):
    form = FinanceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("transactions")

    return render(
        request,
        "finance/transaction_form.html",
        {"form": form},
    )


def edit_transaction(request, pk):
    transaction = get_object_or_404(Finance, pk=pk)

    form = FinanceForm(
        request.POST or None,
        instance=transaction,
    )

    if form.is_valid():
        form.save()
        return redirect("transactions")

    return render(
        request,
        "finance/transaction_form.html",
        {"form": form},
    )


def delete_transaction(request, pk):
    transaction = get_object_or_404(Finance, pk=pk)

    if request.method == "POST":
        transaction.delete()
        return redirect("transactions")

    return render(
        request,
        "finance/transaction_confirm_delete.html",
        {"transaction": transaction},
    )