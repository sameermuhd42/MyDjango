from user.models import TimeSheet
from reporting import models
import django_filters
from django import forms


class TimeSheetFilter(django_filters.Filter):
    user = django_filters.ModelChoiceFilter(queryset=models.CustomUser.objects.all(),
                                            widget=forms.Select(attrs={'class': 'form-select w-50'}))        # To style filter field

    class Meta:
        model = TimeSheet
        fields = ['date', 'batch', 'user']
