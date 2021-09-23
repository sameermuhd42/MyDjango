from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from customer import forms
from owner import models
from customer.filters import BookFilter
from django.contrib import messages

# Create your views here.


def signup_view(request):
    form = forms.UserSignUpForm()
    if request.method == 'POST':
        form = forms.UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request, 'signup1.html', {'form': form})
    return render(request, 'signup1.html', {'form': form})


def signin_view(request):
    form = forms.UserSignInForm()
    if request.method == 'POST':
        form = forms.UserSignInForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_name, password=password)
            if user:
                login(request, user)
                return redirect('userhome')
            else:
                messages.error(request, 'Incorrect username or password')
                return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect('signin')


def user_base(request):
    return render(request, 'simple.html')


def user_home(request):
    books = models.Book.objects.all()
    return render(request, 'user_home.html', context= {'books': books})


def order_create(request, prod_id):
    book = models.Book.objects.get(id=prod_id)
    form = forms.OrderForm(initial={'product': book})
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, 'Order Placed Successfully')
            return redirect('userhome')
    return render(request, 'order.html', context={'form': form})


def book_find(request):
    filters = BookFilter(request.GET, queryset=models.Book.objects.all())
    return render(request, 'bookfilter.html', context={'filters': filters})
