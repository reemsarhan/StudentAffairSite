from urllib import request
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    active_students_count = Student.objects.filter(status='active').count()
    inactive_students_count = Student.objects.filter(status='inactive').count()
    total_students_count = Student.objects.all().count()

    context = {
        'active_students_count': active_students_count,
        'inactive_students_count': inactive_students_count,
        'total_students_count': total_students_count
    }
    return render(request, 'index.html', context)


def base(request):
    allAdmins = User.objects.all()  # Get all students from the database
    context = {'allAdmins': allAdmins}
    return render(request, 'base.html', context)


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
    context = {'student': student}
    return render(request, 'studentInfo.html', context)


def search_results(request):
    search_term = request.GET.get('NameTobeSearched', '')
    students = Student.objects.filter(name__icontains=search_term)
    return render(request, 'searchResults.html', {'students': students})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('students:studentData')


def assign_department(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        department = request.POST.get('dep')
        student.department = department
        student.save()
        return redirect('students:studentData')
    context = {'student': student}
    return render(request, 'studentDepart.html', context)


def studentUpdateByID(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        level = request.POST.get('level')
        email = request.POST.get('Email')
        phoneNum = request.POST.get('mobile')
        # Assuming there's a 'gpa' field in the form
        gpa = request.POST.get('gpa')

        student.level = level
        student.email = email
        student.phoneNumber = phoneNum
        student.gpa = gpa  # Update the GPA field if necessary

        student.save()
        return redirect('students:studentData')

    context = {'student': student}
    return render(request, 'studentUpdate.html', context)
