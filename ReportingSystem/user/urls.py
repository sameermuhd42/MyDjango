from django.urls import path
from user import views


urlpatterns = [
    path('user/index/', views.UserIndex.as_view(), name='userindex'),
    path('user/dash/', views.UserDash.as_view(), name='userdash'),
    path('timesheet/add/', views.TimeSheetAdd.as_view(), name='timesheetadd'),
    path('timesheets/', views.TimeSheetList.as_view(), name='timesheetlist'),
    path('timesheet/update/<int:id>', views.TimeSheetEdit.as_view(), name='timesheetedit'),
    path('timesheet/delete/confirm/<int:id>', views.TimeSheetDelete.as_view(), name='timesheetdelete'),
]
