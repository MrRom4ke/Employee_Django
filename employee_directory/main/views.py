from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Employees, Departments


class DepartmentsTreeView(ListView):
    model = Departments
    template_name = "departments_tree.html"


class EmployeesListView(ListView):
    paginate_by = 2
    context_object_name = 'employees'
    template_name = 'employees_list.html'

    def get_queryset(self):
        self.department = get_object_or_404(Departments, slug=self.kwargs['slug'])
        return Employees.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_name'] = self.department
        return context


class EmployeeDetailView(DetailView):
    model = Employees
    template_name = 'employee_detail.html'
