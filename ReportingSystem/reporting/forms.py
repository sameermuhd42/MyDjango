from reporting.admin import UserCreationForm
from django.forms import ModelForm
from reporting import models
from django import forms


class UserAddForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ['email', 'role', 'password1', 'password2']


class CourseAddForm(ModelForm):
    class Meta:
        model = models.Course
        fields = ['course_name']


class BatchAddForm(ModelForm):
    class Meta:
        model = models.Batch
        fields = ['course', 'batch_name']


