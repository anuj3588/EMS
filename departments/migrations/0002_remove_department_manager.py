# Generated by Django 5.0 on 2023-12-11 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='manager',
        ),
    ]