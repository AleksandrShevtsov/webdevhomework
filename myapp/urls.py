from django.urls import path
from .views import *

urlpatterns = [

    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view()),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
 ]
