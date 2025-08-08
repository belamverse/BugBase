# yourapp/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

from .utils import get_github_access_token, get_github_user_info,create_or_update_user_from_github

User = get_user_model()


class GithubLogin(APIView):
    def get(self, request):
        client_id = settings.GITHUB_CLIENT_ID
        redirect_uri = settings.GITHUB_REDIRECT_URI

        url = 'https://github.com/login/oauth/authorize'
        params = {
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'scope': 'read:user user:email repo',
        }
        return redirect(f"{url}?{urlencode(params)}")


class GithubCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)

        access_token = get_github_access_token(code)
        if not access_token:
            return Response({'error': 'Failed to retrieve access token'}, status=status.HTTP_400_BAD_REQUEST)

        user_data = get_github_user_info(access_token)
        if not user_data:
            return Response({'error': 'Failed to retrieve user info'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = create_or_update_user_from_github(user_data, access_token)

        if user:
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

            query_params = urlencode({
                'access': access,
                'refresh': str(refresh)
                })

            return redirect(f"{settings.FRONTEND_SUCCESS_URL}?{query_params}")
        return redirect(f"{settings.FRONTEND_ERROR_URL}")

