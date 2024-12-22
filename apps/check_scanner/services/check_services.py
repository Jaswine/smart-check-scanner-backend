from typing import List

from django.contrib.auth.models import User

from apps.check_scanner.models import Check


def fild_all_checks() -> List[Check]:
    """
        Get all active checks from the database
        :return: List[Check]
    """
    return Check.objects.all()

def create_check(user: User, file) -> Check:
    """
        Create a new check and save it to the database
        :param user: User object
        :param file: File object
        :return: Check object if successful, None otherwise
    """
    try:
        return Check.objects.create(user=user, file=file)
    except Exception as e:
        print(f"Error creating check: {e}")
        return None