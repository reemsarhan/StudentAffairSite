# Generated by Django 4.2.1 on 2023-05-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[{'Computer Science', 'CS'}, {'IS', 'Information Systems'}, {'Information Technology', 'IT'}, {'DS', 'Decision Support'}], max_length=25),
        ),
    ]
