# Generated by Django 5.0 on 2023-12-11 07:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('employees', '0002_alter_employeedetails_hire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 7, 54, 32, 848184)),
        ),
    ]