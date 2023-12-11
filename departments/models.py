from django.db import models

from employees import models as emp_models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
