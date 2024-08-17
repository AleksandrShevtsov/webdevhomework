from django.urls import path
from .views import *

urlpatterns = [

    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateCreateView.as_view()),
 ]
