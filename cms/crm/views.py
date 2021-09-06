from django.shortcuts import render, redirect
from crm import models
from django.contrib.auth import authenticate, login

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        confirmp = request.POST.get('confirmp')

        if pwd == confirmp:
            user = models.CustUser.objects.create_user(username=uname, email=email, password=pwd)
            user.save()

            return redirect('signin')
    return render(request, 'sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=uname, password=pwd)
        if user is None:
            print("User doesn't exist")
        else:
            print("User exist")
        login(request, user)
        return redirect('emphome')
    return render(request, 'sign_in.html')


def emp_home(request):
    return render(request, 'emp_home.html')


def emp_create(request):
    if request.method == 'GET':
        return render(request, 'emp_add.html')
    elif request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        net_salary = request.POST.get('net_salary')
        print(emp_name, email, phone, net_salary)
        return render(request, 'emp_add.html')


def emp_view(request, id):
    return render(request, 'emp_view.html')


def emp_update(request, id):
    return render(request, 'emp_change.html')


def emp_remove(request, id):
    return render(request, 'emp_remove.html')


def emp_view_all(request):
    return render(request, 'emp_view_all.html')
