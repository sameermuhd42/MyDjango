from reporting.admin import UserCreationForm
from django.forms import ModelForm
from django import forms
from user import models


class TimeSheetAddForm(forms.ModelForm):
    class Meta:
        model = models.TimeSheet
        fields = ['batch', 'topic', 'topic_status']


class TimeSheetEditForm(forms.ModelForm):
    class Meta:
        model = models.TimeSheet
        fields = ['batch', 'topic', 'topic_status']
