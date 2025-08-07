import requests
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_USER_API = 'https://api.github.com/user'


def get_github_access_token(code):
    headers = {'Accept': 'application/json'}
    data = {
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_CLIENT_SECRET,
        'code': code,
        'redirect_uri': settings.GITHUB_REDIRECT_URI,
    }
    response = requests.post(GITHUB_TOKEN_URL, headers=headers, data=data)
    if response.status_code != 200:
        return None
    return response.json().get('access_token')


def get_github_user_info(access_token):
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(GITHUB_USER_API, headers=headers)
    if response.status_code != 200:
        return None
    return response.json()


def create_or_update_user_from_github(data):
    email = data.get('email') or f"{data.get('login')}@github.com"
    user, _ = User.objects.get_or_create(
        email=email,
        defaults={'is_active': True, 'is_staff': False}
    )
    user.username = data.get('login')
    user.first_name = data.get('name', '')
    user.avatar_url = data.get('avatar_url', '')
    user.save(update_fields=['username', 'first_name', 'avatar_url'])
    return user