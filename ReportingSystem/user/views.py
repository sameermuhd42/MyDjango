from django.shortcuts import render
from django.urls import reverse_lazy
from reporting import models
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from reporting import forms
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class UserIndex(TemplateView):
    template_name = 'user/user_index.html'


class UserDash(TemplateView):
    template_name = 'user/user_dash.html'
