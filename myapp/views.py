from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task, SubTask, Category
from .serializers import *


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubTaskListCreateView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
