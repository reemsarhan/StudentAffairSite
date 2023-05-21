# Generated by Django 4.2.1 on 2023-05-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[{'M', 'Male'}, {'Female', 'F'}], max_length=7),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[{'ACTIVE', 'ACtive'}, {'IN-ACTIVE', 'INACTIVE'}], max_length=25),
        ),
    ]
