from django.shortcuts import render, redirect
from customer import forms
from owner import models

# Create your views here.


# def signup_view(request):
#     form = forms.UserRegistrationForm()
#     if request.method == 'POST':
#         form = forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect(request, 'signin')
#         else:
#             return render(request, 'signup1.html', {'form': form})
#     return render(request, 'signup1.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        confirm_password = request.POST.get('confirmp')
        if password == confirm_password:
            user = models.CustomUser.objects.create_user(first_name=fname, username=uname, email=email, password=password)

            user.save()

    return render(request, 'custlogin.html')


def signin_view(request):
    return render(request, 'login.html')


def user_base(request):
    return render(request, 'simple.html')


def user_home(request):
    books = models.Book.objects.all()
    return render(request, 'user_home.html', {'books': books})
