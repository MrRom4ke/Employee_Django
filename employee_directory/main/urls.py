from django.urls import path
from .views import DepartmentsTreeView, EmployeesListView, EmployeeDetailView

urlpatterns = [
    path('', DepartmentsTreeView.as_view(), name='home_page'),
    path('<str:slug>/', EmployeesListView.as_view(), name='employee-at-department'),
    path('<str>/<str:slug>/', EmployeeDetailView.as_view()),
]
