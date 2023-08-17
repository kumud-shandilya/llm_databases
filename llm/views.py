# from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from llm.models import UserPrompt
from llm.serializers import UserPromptSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import asyncio

from llm.Builder_Kshan_py.main import test

@csrf_exempt
@api_view(['POST'])
def prompt_to_query(request):
    if request.method == 'POST':
        # print(request)
        data = request.data
        print(data)
        serializer = UserPromptSerializer(data=data)
        print(f"s = {serializer}")
        if serializer.is_valid():
            print("abab")
            # return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data= asyncio.run(test(serializer.data)), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        return Response("hello", status=status.HTTP_200_OK)
    
