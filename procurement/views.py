from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    PurchaseRequisition,
    PurchaseRequisitionItem,
    SupplierQuotation,
    GoodsReceivedNote,
)

from .forms import (
    PurchaseRequisitionForm,
    PurchaseRequisitionItemForm,
    SupplierQuotationForm,
    GoodsReceivedNoteForm,
)


# ==========================
# DASHBOARD
# ==========================

def dashboard(request):
    context = {
        "requisition_count": PurchaseRequisition.objects.count(),
        "quotation_count": SupplierQuotation.objects.count(),
        "grn_count": GoodsReceivedNote.objects.count(),
        "recent_requisitions": PurchaseRequisition.objects.order_by("-id")[:10],
    }

    return render(request, "procurement/dashboard.html", context)


# ==========================
# PURCHASE REQUISITIONS
# ==========================

def purchase_requisitions(request):
    requisitions = PurchaseRequisition.objects.all().order_by("-id")

    return render(
        request,
        "procurement/purchase_requisitions.html",
        {"requisitions": requisitions},
    )


def add_purchase_requisition(request):
    form = PurchaseRequisitionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("purchase_requisitions")

    return render(
        request,
        "procurement/purchase_requisition_form.html",
        {"form": form},
    )


def edit_purchase_requisition(request, pk):
    requisition = get_object_or_404(PurchaseRequisition, pk=pk)

    form = PurchaseRequisitionForm(
        request.POST or None,
        instance=requisition,
    )

    if form.is_valid():
        form.save()
        return redirect("purchase_requisitions")

    return render(
        request,
        "procurement/purchase_requisition_form.html",
        {"form": form},
    )


def delete_purchase_requisition(request, pk):
    requisition = get_object_or_404(PurchaseRequisition, pk=pk)

    if request.method == "POST":
        requisition.delete()
        return redirect("purchase_requisitions")

    return render(
        request,
        "procurement/purchase_requisition_confirm_delete.html",
        {"requisition": requisition},
    )


# ==========================
# SUPPLIER QUOTATIONS
# ==========================

def supplier_quotations(request):
    quotations = SupplierQuotation.objects.all().order_by("-id")

    return render(
        request,
        "procurement/supplier_quotations.html",
        {"quotations": quotations},
    )


def add_supplier_quotation(request):
    form = SupplierQuotationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("supplier_quotations")

    return render(
        request,
        "procurement/supplier_quotation_form.html",
        {"form": form},
    )


# ==========================
# GOODS RECEIVED NOTES
# ==========================

def goods_received_notes(request):
    notes = GoodsReceivedNote.objects.all().order_by("-id")

    return render(
        request,
        "procurement/goods_received_notes.html",
        {"notes": notes},
    )


def add_goods_received_note(request):
    form = GoodsReceivedNoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("goods_received_notes")

    return render(
        request,
        "procurement/goods_received_note_form.html",
        {"form": form},
    )