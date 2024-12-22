from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from apps.check_scanner.serializers.check_serializers import CheckSerializer, CreateCheckSerializer
from apps.check_scanner.services.check_services import fild_all_checks, create_check
from apps.check_scanner.utils.cache_utils import get_cache, set_cache, delete_cache_by_pattern
from apps.check_scanner.utils.paginator_util import create_paginator
from config import settings


@api_view(['POST', 'GET'])
def list_create_check_view(request):
    base_cache_key = f'check_list_{request.user.username}'
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        cache_key = f'{base_cache_key}_{page}'
        cache_data = get_cache(cache_key)
        if cache_data: return Response(cache_data, status=HTTP_200_OK)
        check_list = fild_all_checks()
        check_list_paginator = create_paginator(check_list, page=page)
        data = CheckSerializer(check_list_paginator, many=True).data
        set_cache(cache_key, data, timeout=settings.CHECK_LIST_CACHE_TIMEOUT)
        return Response(data, status=HTTP_200_OK)
    if request.method == 'POST':
        serializer = CreateCheckSerializer(data=request.data)
        if serializer.is_valid():
            check = create_check(request.user, serializer.validated_data.get('file'))
            # Extract the text from the check if it's not a photo and Save in the database
            # Send the check to the Gemini AI and save the recomendations
            # Update the check status in the database
            delete_cache_by_pattern(base_cache_key)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
