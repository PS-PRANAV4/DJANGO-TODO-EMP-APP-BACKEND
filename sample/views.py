from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from sample.models import Department, employee
from sample.serializer import DepartmentSerializers, EmployeeSerializers


# Create your views here.


@csrf_exempt
def departmentapi(request, id=0):
    if request.method == 'GET':
        department = Department.objects.all()
        department_seri = DepartmentSerializers(department, many=True)
        print(department_seri.data)
        return JsonResponse(department_seri.data, safe=False)
    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializers(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('added succesfully', safe=False)
        return JsonResponse('failed to add', safe=False)
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Department.objects.get(id=department_data['department_id'])
        department_serializers = DepartmentSerializers(department, data=department_data)
        if department_serializers.is_valid():
            department_serializers.save()
            return JsonResponse('updated', safe=False)
        return JsonResponse('failed')
    elif request.method == "DELETE":
        department = Department.objects.get(id=id)
        department.delete()
        return JsonResponse('deleted', safe=False)


@csrf_exempt
def employe(request, id=0):
    if request.method == 'GET':
        emp = employee.objects.all()
        emp_ser = EmployeeSerializers(emp, many=True)
        return JsonResponse(emp_ser.data, safe=False)
    elif request.method == "POST":
        emp_data = JSONParser().parse(request)
        emp_ser = EmployeeSerializers(data=emp_data)
        if emp_ser.is_valid():
            emp_ser.save()
            return JsonResponse('added succesfully', safe=False)
        return JsonResponse('failed to add', safe=False)
    elif request.method == "PUT":
        emp_data = JSONParser().parse(request)
        emp = employee.objects.get(id=emp_data['id'])
        emp_ser = EmployeeSerializers(emp, data=emp_data)
        if emp_ser.is_valid():
            emp_ser.save()
            return JsonResponse('updated', safe=False)
        return JsonResponse('failed')
    elif request.method == "DELETE":
        emp = employee.objects.get(id=id)
        emp.delete()
        return JsonResponse('deleted', safe=False)
