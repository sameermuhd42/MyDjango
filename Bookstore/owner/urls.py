from django.urls import path
from owner import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.admin_base, name='adminbase'),
    path('adminhome/', views.admin_home, name='adminhome'),
    path('accounts/signup/', views.sign_up, name='signup'),
    path('accounts/signin/', views.sign_in, name='signin'),
    # path('books/add/modelform/', views.book_create_modelform, name='modelform'),
    # path('books/add/modelform/', views.book_create_modelform, name='modelform'),
    path('books/add/', views.book_create, name='addbook'),
    path('books/', views.book_list, name='listbook'),
    path('books/view/<int:id>/', views.book_view, name='viewbook'),
    path('books/change/<int:id>/', views.book_update, name='changebook'),
    path('books/remove/<int:id>/', views.book_remove, name='removebook'),
]
