from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.forms import ModelForm
from django import forms
from owner import models


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserSignInForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #     user = User.objects.filter(username=username, password=password)
    #     if user:
    #         pass
    #     else:
    #         msg = "User doesn't exist."
    #         self.add_error('user_name', msg)


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['product', 'address', 'phone']

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'address': forms.Textarea(attrs={'class ': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
        }

