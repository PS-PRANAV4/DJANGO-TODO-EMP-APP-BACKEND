from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def first(request, id=0):
    if request.method == "GET":
        task = Todo.objects.all()
        taskseri = TodoSerializer(task, many=True)
        return JsonResponse(taskseri.data,safe=False)

    elif request.method == "POST":
        todo_data = JSONParser().parse(request)
        todo_seri = TodoSerializer(data=todo_data)
        if todo_seri.is_valid():
            todo_seri.save()
            return JsonResponse('added succesfully',safe=False)
        return JsonResponse('failed to add',safe=False)
    elif request.method == "PUT":
        task_data = JSONParser().parse(request)
        task = Todo.objects.get(id=task_data['id'])
        task_seri = TodoSerializer(task, data=task_data)
        if task_seri.is_valid():
            task_seri.save()
            return JsonResponse('task updated',safe=False)
        return JsonResponse('failed',safe=False)
    elif request.method == "DELETE":
        task = Todo.objects.get(id=id)
        task.delete()
        return JsonResponse('deleted',safe=False)




