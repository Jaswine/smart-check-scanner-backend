from django.urls import path

from apps.check_scanner.views.check import list_create_check_view

urlpatterns = [
    path('checks/', list_create_check_view, name='list-create-check'),
]