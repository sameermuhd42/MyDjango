from django.urls import path
from customer import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.index, name='index'),
]
