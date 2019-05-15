from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import InfoUser, RegisterUserView, CreateUser, TrueUser

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='token_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userinfo/<int:pk>/', InfoUser.as_view(), name='info_user'),
    path('create/', CreateUser.as_view(), name = "create_user"),
    path('status/true/', TrueUser.as_view(), name = "user_status_super_user"),
]
