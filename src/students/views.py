from urllib import request
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def index(request):
    context = {}
    return render(request, 'index.html', context)


def studentList(request):
    allStudents = Student.objects.all()  # Get all students from the database
    context = {'allStudents': allStudents}
    return render(request, 'studentList.html', context)


def studentData(request):
    allStudents = Student.objects.all()  # Get all students from the database
    # Store all students in a dictionary
    # { 'FrontEnd Name': returned value from the database }
    context = {'allStudents': allStudents}
    # Pass the students to the template
    # 'students/studentList.html',
    return render(request, 'studentData.html', context)


def studentUpdate(request):
    return render(request, 'studentUpdate.html')


def studentDepart(request):
    return render(request, 'studentDepart.html')


def studentAddition(request):
    return render(request, 'studentAddition.html')


def studentInfo(request, id):
    studentInfo = Student.objects.get(id=id)
    context = {'studentInfo': studentInfo}
    return render(request, 'studentInfo.html', context)


def student_detail_view(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student
    }
    return render(request, 'studentInfo.html', context)


def assign_department(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        department = request.POST.get('dep')
        student.department = department
        student.save()
        return HttpResponseRedirect(reverse('students:studentInfo', args=[student.id]))
    context = {'student': student}
    return render(request, 'studentDepart.html', context)


def assign_status(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        department = request.POST.get('status')
        student.status = status
        student.save()
        return HttpResponseRedirect(reverse('students:studentInfo', args=[student.id]))
    context = {'student': student}
    return render(request, 'studentList.html', context)
