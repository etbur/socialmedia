from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# from django.http import

# Create your views here.
class index(APIView):
  def get(self,request):
    return Response('hello!')
   
