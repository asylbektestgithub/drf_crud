from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task


@api_view(['GET'])
def my_api_view(request):
    data = {
        'text': 'Hello, my team !'
    }
    return Response(data)

# TODO: Создать представление tasklist, для которого разрешен метод HTTP GET.
#  tasklist должен выдавать список объектов(записей) модели Task в ввиде JSON данных


@api_view(['GET'])
def tasklist_view(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


# TODO: TCP/IP


@api_view(['GET'])
def task_detail_view(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def task_create_view(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({"Created": "Object is created !"})


@api_view(['POST'])
def task_update_view(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return Response({"info":"Object is deleted"})

