from django.urls import path

from .views import auth

urlpatterns = [
    path('sign-in/', auth.sign_in_view, name='sign-in'),
    path('sign-up/', auth.sign_up_view, name='sign-up'),
]