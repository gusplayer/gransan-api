from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from requests import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import generics

def test(request):
    return HttpResponse("test")



from .serializadores import PostSerializer
from ..muro.models import post



class ListModelMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




class PostList(generics.ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer





class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

