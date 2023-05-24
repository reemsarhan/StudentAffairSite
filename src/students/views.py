from urllib import request
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages


def index(request):
    active_students_count = Student.objects.filter(status='ACTIVE').count()
    inactive_students_count = Student.objects.filter(status='INACTIVE').count()
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
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user_name = request.POST.get('name')
        user_status = request.POST.get('status')
        user_birthDate = request.POST.get('birthDate')
        user_gpa = request.POST.get('gpa')
        user_phoneNumber = request.POST.get('phoneNumber')
        user_email = request.POST.get('email')
        user_gender = request.POST.get('gender')
        user_level = request.POST.get('level')
        user_department = request.POST.get('department')
        if user_gender == "Male":
            user_gender = "M"
        elif user_gender == "Female":
            user_gender = "F"
        if user_status == "Active":
            user_status = "ACTIVE"
        elif user_status == "Inactive":
            user_status = "INACTIVE"
        data = Student(id=user_id, name=user_name, status=user_status, birthDate=user_birthDate, gpa=user_gpa,
                       phoneNumber=user_phoneNumber, email=user_email, gender=user_gender, department=user_department, level=user_level)
        data.save()
    messages.success(request, 'Student data saved successfully.')
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


def studentList(request):
    allStudents = Student.objects.all()  # Get all students from the database
    context = {'allStudents': allStudents}
    return render(request, 'studentList.html', context)


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


def updateStudentStatus(request):
    if request.method == 'POST':
        studentId = request.POST.get('studentId')
        status = request.POST.get('status')

        student = Student.objects.get(id=studentId)
        student.status = status
        student.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def search_results(request):
    if 'NameTobeSearched' in request.GET:
        search_name = request.GET['NameTobeSearched']
        students = Student.objects.filter(
            name__istartswith=search_name, status='ACTIVE')
        if students.exists():
            return render(request, 'searchResults.html', {'students': students})
    not_found = True
    return render(request, 'searchResults.html', {'not_found': not_found})
