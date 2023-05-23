from django.db import models

DEPARTMENTS = (
    ('CS', 'Computer Science'),
    ('IS', 'Information Systems'),
    ('IT', 'Information Technology'),
    ('DS', 'Decision Support'),
    ('Gen', 'General'),
)

STATUS = (
    ('ACTIVE', 'Active'),
    ('INACTIVE', 'Inactive')
)

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

LEVEL_CHOICES = (
    (1, 'Level 1'),
    (2, 'Level 2'),
    (3, 'Level 3'),
    (4, 'Level 4'),
)


class Student(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=25, choices=STATUS)
    birthDate = models.DateField()
    gpa = models.FloatField()
    phoneNumber = models.CharField(max_length=11)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=GENDER)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    department = models.CharField(max_length=25, choices=DEPARTMENTS)

    def __str__(self):
        return self.name
