from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/create', create_task, name='create_tasks'),
    path('tasks/list', list_tasks, name='list_tasks'),

]
