# Generated by Django 5.0.dev20230505072651 on 2023-05-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('IS', 'Information Systems'), ('IT', 'Information Technology'), ('DS', 'Decision Support'), ('AI', 'Artificial Intelligence'), ('Gen', 'General')], max_length=25),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.IntegerField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Level 4')]),
        ),
    ]
