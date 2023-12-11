from datetime import datetime

from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeDetails(models.Model):
    DESIGNATION_CHOICES = [
        ('SE', 'Software Engineer'),
        ('SSE', 'Senior Software Engineer'),
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
        ('CEO', 'CEO'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    document = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(['pdf'])])
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    department = models.ForeignKey("departments.Department", on_delete=models.CASCADE, null=True)
    salaries = models.CharField(max_length=225)
    hire_date = models.DateTimeField(default=datetime.now())
    last_working_day = models.DateTimeField(null=True)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='manager')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee} {self.designation}"


class Tasks(models.Model):
    TASKS_STATUS = [
        ('ASSIGNED', 'Assigned'),
        ('COMPLETED', 'Completed'),
        ('WIP', 'Work in Progress'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    assign = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TASKS_STATUS)
    assign_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.description}"
