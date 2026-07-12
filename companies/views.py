from django.shortcuts import render, redirect, get_object_or_404

from .models import Company
from .forms import CompanyForm


def dashboard(request):
    companies = Company.objects.all()

    return render(
        request,
        "companies/dashboard.html",
        {
            "companies": companies,
            "company_count": companies.count(),
        },
    )


def companies(request):
    companies = Company.objects.all()

    return render(
        request,
        "companies/companies.html",
        {"companies": companies},
    )


def add_company(request):
    form = CompanyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("companies")

    return render(
        request,
        "companies/company_form.html",
        {"form": form},
    )


def edit_company(request, pk):
    company = get_object_or_404(Company, pk=pk)

    form = CompanyForm(
        request.POST or None,
        instance=company,
    )

    if form.is_valid():
        form.save()
        return redirect("companies")

    return render(
        request,
        "companies/company_form.html",
        {"form": form},
    )


def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if request.method == "POST":
        company.delete()
        return redirect("companies")

    return render(
        request,
        "companies/company_confirm_delete.html",
        {"company": company},
    )