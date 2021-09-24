from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from reporting import models
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from reporting import forms

# Create your views here.


class AdminIndex(TemplateView):
    template_name = 'reporting/index.html'


class AdminDash(TemplateView):
    template_name = 'reporting/admin_dash.html'


# class AdminHome(TemplateView):
#     template_name = 'reporting/admin_home.html'

    # def get(self, request, *args, **kwargs):      # optional fn. get() also works by using template_name variable
    #     return render(request, self.template_name)


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


class UserList(ListView):
    model = models.CustomUser
    context_object_name = 'users'
    template_name = 'reporting/user_list.html'


class UserEdit(UpdateView):
    form_class = forms.UserAddForm
    model = models.CustomUser
    pk_url_kwarg = 'id'                             # change the value pk to id. default value is pk, used to refer id field in the model
    template_name = 'reporting/user_edit.html'
    success_url = reverse_lazy('userlist')


class CourseAdd(CreateView):
    form_class = forms.CourseAddForm
    model = models.Course
    template_name = 'reporting/course_add.html'
    success_url = reverse_lazy('courselist')


class CourseList(ListView):
    model = models.Course
    context_object_name = 'courses'
    template_name = 'reporting/course_list.html'

    # def get(self, request, *args, **kwargs):          # optional fn. gett() also works by using model, template_name variables
    #     courses = self.model.objects.all()
    #     return render(request, self.template_name, context={'courses': courses})


class CourseEdit(UpdateView):
    form_class = forms.CourseAddForm
    model = models.Course
    pk_url_kwarg = 'id'                             # change the value pk to id. default value is pk, used to refer id field in the model
    template_name = 'reporting/course_edit.html'
    success_url = reverse_lazy('courselist')


class BatchAdd(CreateView):
    form_class = forms.BatchAddForm
    model = models.Batch
    template_name = 'reporting/batch_add.html'
    success_url = reverse_lazy('batchlist')


class BatchList(ListView):
    model = models.Batch
    context_object_name = 'batches'
    template_name = 'reporting/batch_list.html'


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
