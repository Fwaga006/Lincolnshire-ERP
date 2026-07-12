from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm


def dashboard(request):
    employees = Employee.objects.all()

    context = {
        "employees": employees,
        "employee_count": employees.count(),
        "department_count": Department.objects.count(),
    }

    return render(request, "employees/dashboard.html", context)


def employees(request):
    employees = Employee.objects.all()

    return render(
        request,
        "employees/employees.html",
        {"employees": employees},
    )


def add_employee(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("employees")

    return render(
        request,
        "employees/employee_form.html",
        {"form": form},
    )


def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    form = EmployeeForm(
        request.POST or None,
        request.FILES or None,
        instance=employee,
    )

    if form.is_valid():
        form.save()
        return redirect("employees")

    return render(
        request,
        "employees/employee_form.html",
        {"form": form},
    )


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect("employees")

    return render(
        request,
        "employees/employee_confirm_delete.html",
        {"employee": employee},
    )