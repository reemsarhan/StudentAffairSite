from django.db import models

Departments = (
    {'CS', 'Computer Science'},
    {'IS', 'Information Systems'},
    {'IT', 'Information Technology'},
    {'DS', 'Decision Support'},
    {'Gen', 'General'},
)

Status = (
    {'ACTIVE', 'Active'},
    {'INACTIVE', 'InActive'}
)

Gender = ({'M', 'Male'},
          {'F', 'Female'}
          )
# Model for Student


class Student(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=25, choices=Status)
    birthDate = models.DateField()
    gpa = models.FloatField()
    phoneNumber = models.CharField(max_length=11)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=Gender)
    level = models.CharField(max_length=1)
    department = models.CharField(max_length=25, choices=Departments)

    def __str__(self):
        return self.name
