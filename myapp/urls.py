from django.urls import path
from .views import *

urlpatterns = [

    path('tasks/', TaskListCreateView.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='tasks-detail-update-delete'),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
 ]
