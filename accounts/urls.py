from django.urls import path
from .views import (
    GithubLogin,
    GithubCallback,
)

urlpatterns = [
    path('github/login/', GithubLogin.as_view(),name='github-login'),
    path('github/callback/', GithubCallback.as_view(), name='github-callback'),
]
