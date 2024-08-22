from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('subtasks', SubTaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
 ]
