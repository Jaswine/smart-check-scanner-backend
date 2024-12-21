from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN)

from apps.user.serializers.user_serializers import UserSignInSerializer, UserSignUpSerializer
from apps.user.services.user_services import (get_user_by_email,
                                              user_check_password_by_user, get_user_by_username, create_user)
from apps.user.utils.token_utils import generate_tokens


@api_view(['POST'])
def sign_in_view(request):
    """
        Endpoint for user login
    """
    serializer = UserSignInSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors,
                    status=HTTP_400_BAD_REQUEST)

    user = get_user_by_email(serializer.validated_data.get('email'))

    if not user:
        return Response({
            'message': 'User not found!'
        }, status=HTTP_401_UNAUTHORIZED)

    if not user_check_password_by_user(user,
                                       serializer.validated_data.get('password')):
        return Response({
            'message': 'Incorrect password!'
        }, status=HTTP_403_FORBIDDEN)

    access, refresh = generate_tokens(user)

    return Response({
        'access': access,
        'refresh': refresh
    }, status=HTTP_200_OK)

@api_view(['POST'])
def sign_up_view(request):
    """
        Endpoint for user registration
    """
    serializer = UserSignUpSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors,
                    status=HTTP_400_BAD_REQUEST)

    if get_user_by_username(serializer.validated_data.get('username')):
        return Response({
            'detail': 'User with this username already exists.'
        }, status=HTTP_400_BAD_REQUEST)

    if get_user_by_email(serializer.validated_data.get('email')):
        return Response({
            'detail': 'User with this email already exists.'
        }, status=HTTP_400_BAD_REQUEST)

    user = create_user(serializer.validated_data.get('username'),
                       serializer.validated_data.get('email'),
                       serializer.validated_data.get('password'))
    if not user:
        return Response({
            'detail': 'Failed to create user.'
        }, status=HTTP_400_BAD_REQUEST)
    access, refresh = generate_tokens(user)
    return Response({
        'access': access,
        'refresh': refresh
    }, status=HTTP_200_OK)