from django.urls import path
from maths import views

urlpatterns = [
    path('', views.home, name='home'),
    path('djangoforms/', views.django_forms, name='dforms'),
    path('addnum/', views.add_numbers, name='addnum'),
    path('subnum/', views.sub_numbers, name='subnum'),
    path('mulnum/', views.mul_numbers, name='mulnum'),
    path('divnum/', views.div_numbers, name='divnum'),
    path('cubnum/', views.cub_numbers, name='cubnum'),
]
