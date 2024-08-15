from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/create', create_task, name='create_tasks'),
    path('tasks/', list_tasks, name='list_tasks'),
    path('tasks/stats', task_stats, name='task_stats'),
    path('tasks/<int:pk>', task_details, name='task_details'),

]
