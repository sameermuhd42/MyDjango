from django.shortcuts import render, redirect
from customer import forms

# Create your views here.


def signup_view(request):
    form = forms.UserRegistrationForm()
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(request, 'signin')
        else:
            return render(request, 'signup1.html', {'form': form})
    return render(request, 'signup1.html', {'form': form})


def signin_view(request):
    return render(request, 'login.html')
