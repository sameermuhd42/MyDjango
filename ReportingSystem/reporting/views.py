from django.shortcuts import render, redirect
from reporting import models
from django.views.generic import TemplateView
from reporting import forms

# Create your views here.


class AdminHome(TemplateView):
    template_name = 'reporting/admin_home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserAdd(TemplateView):
    template_name = 'reporting/user_add.html'
    model = models.CustomUser

    def get(self, request, *args, **kwargs):
        form = forms.UserAddForm
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = forms.UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminhome')








# def sign_up(request):
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         email = request.POST.get('email')
#         pwd = request.POST.get('pwd')
#         confirmp = request.POST.get('confirmp')
#         role = request.POST.get('role')
#
#         if pwd == confirmp:
#             user = models.CustUser.objects.create_user(username=uname, email=email, password=pwd, role=role)
#             user.save()
#
#             return redirect('/home/login2/')
#     return render(request, 'regn.html')
