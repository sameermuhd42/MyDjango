from django.shortcuts import render

# Create your views here.


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
    return  render(request, 'emp_view.html')


def emp_update(request, id):
    return render(request, 'emp_change.html')


def emp_remove(request, id):
    return render(request, 'emp_remove.html')


def emp_view_all(request):
    return render(request, 'emp_view_all.html')
