from django.shortcuts import redirect, render
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView as login, LogoutView as logout

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('status/', views.studentList),
    path('login/', login.as_view(template_name='login.html'), name='login'),
    path('logout/', logout.as_view(), name='logout'),
    path('add/', views.studentAddition),
    path('<int:id>/', views.studentInfo, name='studentInfo'),
    path('update/', views.studentUpdate),
    path('assigndep/', views.studentDepart),
    path('students/<int:id>/', views.student_detail_view, name='studentInfo'),
    path('assign-department/<int:id>/',
         views.assign_department, name='assign-department'),
]
