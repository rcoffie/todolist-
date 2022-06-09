from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from task.models import Task
from task.permissions import AuthOwnerDeleteUpdate
from task.serializers import TaskSerializer
from task.pagination import TodoListPagination, StandardResultsSetPagination
from rest_framework.pagination import PageNumberPagination

# Create your views here.

# list todo
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def task_list(request):

    tasks = Task.objects.all().filter(owner=request.user)
    if len(tasks) > 0:
        paginator = StandardResultsSetPagination()
        task_page = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(tasks, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({}, status=status.HTTP_200_OK)


# create todo
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_task(request):
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# todo details
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)


# update todo
@api_view(["GET", "PUT"])
@permission_classes([AuthOwnerDeleteUpdate])
def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializser.errors, status=status.HTTP_404_BAD_REQUEST)


# delete todo
@api_view(["GET", "DELETE"])
@permission_classes([AuthOwnerDeleteUpdate])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == "DELETE":
        return Response(status=204)
