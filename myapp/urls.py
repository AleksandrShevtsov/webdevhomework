from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from myapp.views.user_views import UserListGenericView, RegisterUserGenericView, LoginView, LogoutView, \
    ProtectedDataView
from myapp.views.views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('subtasks', SubTaskViewSet)
# router.register('users', UserListGenericView)
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListGenericView.as_view()),
    path('register/', RegisterUserGenericView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('protected/', ProtectedDataView.as_view()),

 ]
