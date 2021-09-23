from django.urls import path
from customer import views


urlpatterns = [
    path('account/signup', views.signup_view, name='signup'),
    path('account/signin', views.signin_view, name='signin'),
    path('account/signout', views.signout_view, name='signout'),
    path('', views.user_base, name='userbase'),
    path('userhome', views.user_home, name='userhome'),
    path('books/order/add/<int:prod_id>', views.order_create, name='ordercreate')
]