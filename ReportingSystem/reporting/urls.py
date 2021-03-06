from django.urls import path
from reporting import views

urlpatterns = [
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/logout/', views.Logout.as_view(), name='logout'),
    path('index/', views.AdminIndex.as_view(), name='adminindex'),
    path('admin/dash/', views.AdminDash.as_view(), name='admindash'),
    path('user/add/', views.UserAdd.as_view(), name='useradd'),
    path('users/', views.UserList.as_view(), name='userlist'),
    path('users/update/<int:id>', views.UserEdit.as_view(), name='useredit'),
    path('course/add/', views.CourseAdd.as_view(), name='courseadd'),
    path('courses/', views.CourseList.as_view(), name='courselist'),
    path('courses/update/<int:id>', views.CourseEdit.as_view(), name='courseedit'),
    path('batch/add/', views.BatchAdd.as_view(), name='batchadd'),
    path('batches/', views.BatchList.as_view(), name='batchlist'),
    path('batches/update/<int:id>', views.BatchEdit.as_view(), name='batchedit'),
    path('timesheets/', views.AdminTimeSheetList.as_view(), name='admintimesheetlist'),
    path('timesheet/verify/<int:id>', views.TimeSheetVerify.as_view(), name='timesheetverify')
]
