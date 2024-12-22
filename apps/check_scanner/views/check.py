from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from apps.check_scanner.serializers.check_serializers import CheckSerializer, CreateCheckSerializer
from apps.check_scanner.services.check_services import fild_all_checks, check_handling
from apps.check_scanner.utils.cache_utils import get_cache, set_cache, delete_cache_by_pattern
from apps.check_scanner.utils.paginator_util import create_paginator
from config import settings


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list_create_check_view(request):
    """
        End point for displaying the list of checks
    """
    if request.method == 'GET':
        """
            Endpoint for displaying the list of checks with pagination and caching
        """
        base_cache_key = f'check_list_{request.user.username}'
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
        """
            Endpoint for creating a check
        """
        file = request.FILES.get('file')
        if file:
            if not file.name.endswith('.pdf'):
                return Response({
                      'message': 'Document must be a PDF file'
                 }, status=HTTP_400_BAD_REQUEST)
            if check := check_handling(request.user, file):
                delete_cache_by_pattern(f'check_list_{request.user.username}')
                serializer = CheckSerializer(check, many=False)
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response({
                 'message': 'Failed to create check'
            }, status=HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'Failed to create check'
        }, status=HTTP_400_BAD_REQUEST)