from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


def generate_tokens(user: User) -> (str, str):
    """
        Generate access and refresh tokens for the user
        :param: user - User
        :return: Tuple of access and refresh tokens
    """
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token), str(refresh)