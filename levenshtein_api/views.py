from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .functions import *

import time


class API_Levin(APIView):
    def get(self, request):
        s1 = request.GET.get('s1', None)
        s2 = request.GET.get('s2', None)

        if request.GET.get('gen', False):
            len_s = request.GET.get('len', 10000)

            s1 = generate_string(len_s)
            s2 = generate_string(len_s)


        func = request.GET.get('func', None)

        if s1 is None or s2 is None or func is None:
            content = {'info': 's1, s2 and function is required'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        start_time = time.time()
        levin_len = None

        if str(func) == 'wiki':
            levin_len = distance_levin_wiki(s1, s2)
        elif str(func) == 'rec':
            levin_len = distance_levin_rec(s1, s2)
        else:
            content = {'info': 'function not found'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        serializer = LevinSerializer(
            Levin(
                s1, s2, levin_len, time.time() - start_time
            )
        )

        return JsonResponse(serializer.data)
