from django.core.paginator import Paginator

from apps.check_scanner.models import Check
from config import settings


def create_paginator(courses: list[Check] = list, /, *, page: int = 1) -> list:
    """
        Paginator for the given checks
        :param courses: list[Check] - Check list
        :param page: int - page number
        :return Check list
    """
    paginator = Paginator(courses, settings.PAGINATOR_PAGE_SIZE)
    return paginator.get_page(page)