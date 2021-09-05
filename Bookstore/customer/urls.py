from django.urls import path
from customer import views


urlpatterns = [
    path('account/signup/', views.signup_view, name='signup'),
    path('account/signin/', views.signin_view, name='signin'),
]