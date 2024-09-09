from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from myapp.views.user_views import UserListGenericView, RegisterUserGenericView, LoginView, LogoutView, \
    ProtectedDataView
from myapp.views.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Task API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=[AllowAny,],

)

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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

 ]
