from django.shortcuts import redirect,render
from django.urls import path
from . import views

app_name = 'students'


urlpatterns = [
    path('', views.studentData),
    path('status/', views.studentList),
    path('add/', views.studentAddition),
    path('<int:id>/', views.studentInfo, name='studentInfo'),
    path('update/', views.studentUpdate),
    path('assigndep/', views.studentDepart),
    path('students/<int:id>/', views.student_detail_view, name='studentInfo'),
    path('assign-department/<int:id>/', views.assign_department, name='assign-department'),
       
 

]
