from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from user import models
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from user import forms
from django.contrib.auth import authenticate, login, logout
from reporting.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(login_required, name='dispatch')
class UserIndex(TemplateView):
    template_name = 'user/user_index.html'


@method_decorator(login_required, name='dispatch')
class UserDash(TemplateView):
    template_name = 'user/user_dash.html'


@method_decorator(login_required, name='dispatch')
class TimeSheetAdd(CreateView):
    form_class = forms.TimeSheetAddForm
    model = models.TimeSheet
    template_name = 'user/timesheet_add.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            time_sheet = form.save(commit=False)
            time_sheet.user = request.user
            time_sheet.save()
            return redirect('timesheetlist')


@method_decorator(login_required, name='dispatch')
class TimeSheetList(ListView):
    model = models.TimeSheet
    context_object_name = 'timesheets'
    template_name = 'user/timesheet_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset


@method_decorator(login_required, name='dispatch')
class TimeSheetEdit(UpdateView):
    form_class = forms.TimeSheetEditForm
    model = models.TimeSheet
    pk_url_kwarg = 'id'                             # change the value pk to id. default value is pk, used to refer id field in the model
    template_name = 'user/timesheet_edit.html'
    success_url = reverse_lazy('timesheetlist')


@method_decorator(login_required, name='dispatch')
class TimeSheetDelete(UpdateView):
    model = models.TimeSheet
    pk_url_kwarg = 'id'
    template_name = 'user/timesheet_edit.html'
    success_url = reverse_lazy('timesheetlist')
