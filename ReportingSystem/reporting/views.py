from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from reporting import models
from user.models import TimeSheet
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from reporting import forms
from reporting.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class Login(TemplateView):
    form_class = forms.LoginForm
    template_name = 'reporting/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                if request.user.is_staff:
                    return redirect('admindash')
                else:
                    return redirect('userdash')


@method_decorator(login_required, name='dispatch')
class Logout(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


@method_decorator(login_required, name='dispatch')
class AdminIndex(TemplateView):
    template_name = 'reporting/index.html'


@method_decorator(login_required, name='dispatch')
class AdminDash(TemplateView):
    template_name = 'reporting/admin_dash.html'


# class AdminHome(TemplateView):
#     template_name = 'reporting/admin_home.html'

    # def get(self, request, *args, **kwargs):      # optional fn. get() also works by using template_name variable
    #     return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class UserAdd(CreateView):
    form_class = forms.UserAddForm
    model = models.CustomUser
    template_name = 'reporting/user_add.html'
    success_url = reverse_lazy('userlist')         # redirect html page

    def get(self, request, *args, **kwargs):        # optional fn. get() also works by using template_name, form_class variables
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):       # optional fn. post() also works by using form_class, model, success_url variables
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlist')


@method_decorator(login_required, name='dispatch')
class UserList(ListView):
    model = models.CustomUser
    context_object_name = 'users'
    template_name = 'reporting/user_list.html'


@method_decorator(login_required, name='dispatch')
class UserEdit(UpdateView):
    form_class = forms.UserAddForm
    model = models.CustomUser
    pk_url_kwarg = 'id'                             # change the value pk to id. default value is pk, used to refer id field in the model
    template_name = 'reporting/user_edit.html'
    success_url = reverse_lazy('userlist')


@method_decorator(login_required, name='dispatch')
class CourseAdd(CreateView):
    form_class = forms.CourseAddForm
    model = models.Course
    template_name = 'reporting/course_add.html'
    success_url = reverse_lazy('courselist')

    # def get_context_data(self, **kwargs):           # To add extra context in a specific type of view by get() method
    #     context = super().get_context_data(**kwargs)
    #     context['courses'] = self.model.objects.all()
    #     return context


@method_decorator(login_required, name='dispatch')
class CourseList(ListView):
    model = models.Course
    context_object_name = 'courses'
    template_name = 'reporting/course_list.html'

    # def get(self, request, *args, **kwargs):          # optional fn. gett() also works by using model, template_name variables
    #     courses = self.model.objects.all()
    #     return render(request, self.template_name, context={'courses': courses})


@method_decorator(login_required, name='dispatch')
class CourseEdit(UpdateView):
    form_class = forms.CourseAddForm
    model = models.Course
    pk_url_kwarg = 'id'                             # change the value pk to id. default value is pk, used to refer id field in the model
    template_name = 'reporting/course_edit.html'
    success_url = reverse_lazy('courselist')


@method_decorator(login_required, name='dispatch')
class BatchAdd(CreateView):
    form_class = forms.BatchAddForm
    model = models.Batch
    template_name = 'reporting/batch_add.html'
    success_url = reverse_lazy('batchlist')


@method_decorator(login_required, name='dispatch')
class BatchList(ListView):
    model = models.Batch
    context_object_name = 'batches'
    template_name = 'reporting/batch_list.html'


@method_decorator(login_required, name='dispatch')
class BatchEdit(UpdateView):
    form_class = forms.BatchAddForm
    model = models.Batch
    pk_url_kwarg = 'id'                             # change the value pk to id. default value is pk, used to refer id field in the model
    template_name = 'reporting/batch_edit.html'
    success_url = reverse_lazy('batchlist')


# Edit when using TemplateView
# class BatchEdit(TemplateView):
#     form_class = forms.BatchAddForm
#     model = models.Batch
#     template_name = 'reporting/batch_edit.html'
#
#     def get(self, request, *args, **kwargs):
#         batch_id = kwargs.get('id')
#         batch = self.model.objects.get(id=batch_id)
#         form = self.form_class(instance=batch)
#         return render(request, self.template_name, context={'form': form})
#
#     def post(self, request, *args, **kwargs):
#         batch_id = kwargs.get('id')
#         batch = self.model.objects.get(id=batch_id)
#         form = self.form_class(request.POST, instance=batch)
#         if form.is_valid():
#             form.save()
#             return redirect('batchlist')


@method_decorator(login_required, name='dispatch')
class AdminTimeSheetList(ListView):
    model = TimeSheet
    context_object_name = 'timesheets'
    template_name = 'reporting/admin_timesheet_list.html'

    # def get_queryset(self):
    #     queryset = self.model.objects.all()
    #     return queryset


@method_decorator(login_required, name='dispatch')
class TimeSheetVerify(TemplateView):
    model = TimeSheet
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        time_sheet = self.model.objects.get(id=kwargs.get('id'))
        time_sheet.is_verified = True
        time_sheet.save()
        return redirect('admintimesheetlist')





# def sign_up(request):
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         email = request.POST.get('email')
#         pwd = request.POST.get('pwd')
#         confirmp = request.POST.get('confirmp')
#         role = request.POST.get('role')
#
#         if pwd == confirmp:
#             user = models.CustUser.objects.create_user(username=uname, email=email, password=pwd, role=role)
#             user.save()
#
#             return redirect('/home/login2/')
#     return render(request, 'regn.html')
