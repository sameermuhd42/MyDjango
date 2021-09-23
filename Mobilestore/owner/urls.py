from django.urls import path
from owner import views


urlpatterns = [
    path('', views.base_owner, name='base'),
]
