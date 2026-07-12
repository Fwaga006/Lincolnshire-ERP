from django.shortcuts import render


def dashboard(request):
    return render(request, "business_reports/dashboard.html")