from django.urls import path
from crm import views

urlpatterns = [
    path('employees/add/', views.emp_create, name='addemp'),
    path('employees/<int:id>/', views.emp_view, name='viewemp'),
    path('employees/change/<int:id>/', views.emp_update, name='changeemp'),
    path('employees/remove/<int:id>/', views.emp_remove, name='removeemp'),
    path('employees/', views.emp_view_all, name='viewallemp'),
]
