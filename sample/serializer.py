from rest_framework import serializers
from . models import Department,employee


class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'department_name',)


class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = employee
        fields = ('id', 'employee_name', 'employee_departmen', 'date_of_joining')