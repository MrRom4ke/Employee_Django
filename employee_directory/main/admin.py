from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Departments, Employees


class DepartmentsAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Departments, DepartmentsAdmin)


class EmployeesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Employees, EmployeesAdmin)
