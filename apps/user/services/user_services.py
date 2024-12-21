from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

def get_user_by_username(username: str) -> User | None:
    """
        Get a user by email
        :param: username
        :return: User object
    """
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None

def get_user_by_email(email: str) -> User | None:
    """
        Get a user by email
        :param: email
        :return: User object
    """
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None

def create_user(username: str, email: str, password: str) -> User | None:
    """
        Create a new user
        :param username: Username
        :param email: Email
        :param password: Password
        :return: User instance
    """
    try:
        return User.objects.create(username=username,
                                   email=email,
                                   password=make_password(password))
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

def user_check_password_by_user(user: User, password: str) -> True | False:
    """
        Check if the provided password matches the user's password
        :param user: User object
        :param password: Password provided by the user
        :return: True if password matches, False otherwise
    """
    return user.check_password(password)