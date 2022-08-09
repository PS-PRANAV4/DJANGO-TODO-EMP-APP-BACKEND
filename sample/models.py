from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=100)


class employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_departmen = models.CharField(max_length=100)
    date_of_joining = models.DateField()
