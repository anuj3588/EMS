# Generated by Django 5.0 on 2023-12-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_remove_department_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
