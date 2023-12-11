# Generated by Django 5.0 on 2023-12-11 07:49

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=13)),
                ('document', models.FileField(upload_to='')),
                ('designation', models.CharField(choices=[('SE', 'Software Engineer'), ('SSE', 'Senior Software Engineer'), ('TL', 'Team Lead'), ('Manager', 'Manager')], max_length=20)),
                ('salaries', models.CharField(max_length=225)),
                ('hire_date', models.DateTimeField(default=datetime.datetime(2023, 12, 11, 7, 49, 9, 800105))),
                ('last_working_day', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('ASSIGNED', 'Assigned'), ('COMPLETED', 'Completed'), ('WIP', 'Work in Progress')], max_length=25)),
                ('assign_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
