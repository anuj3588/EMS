# forms.py
from django import forms
from django.core.validators import FileExtensionValidator

from employees.models import Employee


class EmpRegister(forms.Form):
    first_name = forms.CharField(label='Name', max_length=50)
    last_name = forms.CharField(label='last_name', max_length=50)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label="Address", max_length=225)
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    document = forms.FileField(label='Document', validators=[FileExtensionValidator(['pdf'])])
    department = forms.CharField(label='department', max_length=20, required=False)

