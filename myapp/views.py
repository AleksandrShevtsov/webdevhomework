from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import *

from .models import Task, SubTask, Category
from .serializers import *


@api_view(['POST'])
def create_task(request):
    serializer = TaskCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_tasks(request):
    tasks = Task.objects.all()

    status = request.query_params.get('status')
    if status:
        tasks = tasks.filter(status=status)

    deadline = request.query_params.get('deadline')
    if deadline:
        tasks = tasks.filter(deadline__lte=deadline)

    paginator = PageNumberPagination()
    paginator.page_size = 10
    paginated_tasks = paginator.paginate_queryset(tasks, request)

    serializer = TaskSerializer(paginated_tasks, many=True)
    return paginator.get_paginated_response(serializer.data)
