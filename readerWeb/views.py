from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import generics
from rest_framework.views import APIView

from SimpleDjango.utils.Response import JsonResponse
from readerWeb.models import ReadCommend
from readerWeb.serializer import ReadCommendSerializer


class ReadCommendList(generics.ListCreateAPIView):
    queryset = ReadCommend.objects.all()
    serializer_class = ReadCommendSerializer


class ReadCommendItem(APIView):
    def get(self, request):
        try:
            query_set = ReadCommend.objects.all()
            token = request.GET['token']
            commends = query_set.filter(token=token).filter(status=None).first()
            print(commends)
            if commends is None:
                return JsonResponse(code=2, desc='not data')

            if commends.chipId is None:
                return JsonResponse(code=3, desc='Not found chipId')
            # update status = 0
            query_set.filter(token=token).filter(status=None).update(status=0)
            serializers = ReadCommendSerializer(commends)
            return JsonResponse(code=0, desc='success', data=serializers.data)
        except Exception as msg:
            print(msg)
            return JsonResponse(code=1, desc=msg.args[0])
