from django.contrib.admin import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from myapp.serializers import *


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class SubTaskViewSet(ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    @action()
    def count_subtasks(self, request, pk=None):
        task = self.get_object()
        subtask_count = task.subtasks.count()
        return Response({'count': subtask_count})

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action()
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = category.tasks.count()
        return Response({'count': task_count})
