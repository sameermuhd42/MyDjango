from django import forms
from owner import models


class SignUpForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        # Refer Form class by super()(parent) and call clean() method of it, which returns a cleaned_data dictionary
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if age < 0:
            msg = 'Invalid Age'
            self.add_error('age', msg)
        if password != confirm_password:
            msg = "Password doesn't match"
            self.add_error('confirm_password', msg)


class SignInForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        print('valid')


# class BookUpdateForm(forms.Form):
#     book_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     copies = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     def clean(self):
#         print('valid')


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'copies': forms.NumberInput(attrs={'class': 'form-control'})
        }
        label = {
            'book_name': 'Book Name',
            'author': 'Author',
            'price': 'Price',
            'copies': 'Copies'
        }

    def clean(self):
        print('valid')


class BookEditForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

    def clean(self):
        print('valid')
