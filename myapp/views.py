from django.core.paginator import Paginator
from django.db.models import *
from django.utils import timezone
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


# Создайте эндпойнт для получения списка задач с фильтрацией по статусу и дедлайну. Реализуйте пагинацию результатов.
#
# Шаги для выполнения:
#
# Создайте представление для получения списка задач с фильтрами и пагинацией.
#
# Создайте маршрут для обращения к представлению.
@api_view(['GET'])
def list_tasks(request):
    tasks = Task.objects.filter(status__in=['New', 'In progress'], deadline__gt=timezone.now())
    paginator = PageNumberPagination()
    paginator.page_size = 2  # Количество элементов на странице
    result_page = paginator.paginate_queryset(tasks, request)
    serializer = TaskSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def task_stats(request):
    total_tasks = Task.objects.count()
    status_counts = Task.objects.values('status').annotate(count=Count('status'))
    overdue_tasks = Task.objects.filter(deadline__lt=timezone.now(), status__in=['New', 'In progress']).count()

    return Response({
        'total_tasks': total_tasks,
        'status_counts': status_counts,
        'overdue_tasks': overdue_tasks
    })
