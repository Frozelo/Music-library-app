from django.urls import path
from rest_framework.routers import SimpleRouter

from src.api.user.views import CreateUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/register', CreateUserView.as_view(), name='register'),
    path('users/auth', obtain_auth_token, name='api_token_auth'),
]
