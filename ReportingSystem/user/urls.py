from django.urls import path
from user import views


urlpatterns = [
    path('user/index/', views.UserIndex.as_view(), name='userindex'),
    path('user/dash', views.UserDash.as_view(), name='userdash'),
    ]