from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from requests import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


def test(request):
    return HttpResponse("test")

@api_view(['POST',])
def login(request):
    data = request.data
    if(data.get("usuario",None)==None or data.get("contrasena",None)==None):
        return HttpResponse("")
    return JsonResponse(data)
