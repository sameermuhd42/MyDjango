from django.shortcuts import render
from maths import forms
# from maths.forms import CalcForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


# Demonstration of add view using Django forms
def django_forms(request):
    form = forms.CalcForm
    # form = CalcForm
    if request.method == 'POST':
        form = forms.CalcForm(request.POST)
        # form_empty = forms.CalcForm
        if form.is_valid():
            # print(form.cleaned_data)
            num1 = form.cleaned_data.get('num1')
            num2 = form.cleaned_data.get('num2')
            add = num1 + num2
            res = 'Sum = ' + str(add)
            return render(request, 'django_forms.html', {'form': form, 'result': res})
    return render(request, 'django_forms.html', {'form': form})


def add_numbers(request):
    if request.method == 'GET':
        return render(request, 'addition.html')
    elif request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        add = num1 + num2
        res = 'Sum = ' + str(add)
        # context = dict()
        # context['result'] = res
        return render(request, 'addition.html', {'result': res})


def sub_numbers(request):
    if request.method == 'GET':
        return render(request, 'addition.html')
    elif request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        sub = num1 - num2
        res = 'Difference = ' + str(sub)
        # context = dict()
        # context['result'] = res
        return render(request, 'addition.html', {'result': res})


def mul_numbers(request):
    if request.method == 'GET':
        return render(request, 'addition.html')
    elif request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        sub = num1 * num2
        res = 'Product = ' + str(sub)
        # context = dict()
        # context['result'] = res
        return render(request, 'addition.html', {'result': res})


def div_numbers(request):
    if request.method == 'GET':
        return render(request, 'addition.html')
    elif request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        sub = num1 / num2
        res = 'Quotient = ' + str(sub)
        # context = dict()
        # context['result'] = res
        return render(request, 'addition.html', {'result': res})


def cub_numbers(request):
    if request.method == 'GET':
        return render(request, 'addition.html')
    elif request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        cub = num1 * num1 * num1
        res = 'Cube of ' + str(num1) + ' = ' + str(cub)
        # context = dict()
        # context['result'] = res
        return render(request, 'addition.html', {'result': res})
