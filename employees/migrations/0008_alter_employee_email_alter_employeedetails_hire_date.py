# Generated by Django 5.0 on 2023-12-11 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_employeedetails_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 14, 9, 9, 402418)),
        ),
    ]
