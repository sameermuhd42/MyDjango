from django.urls import path
from reporting import views

urlpatterns = [
    path('home/', views.AdminHome.as_view(), name='adminhome'),
    path('user/add/', views.UserAdd.as_view(), name='useradd'),
]
