from django.shortcuts import render
from .serializers import UserInfoSerializer
from rest_framework import viewsets
from .models import UserInfo
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

class userViewSet(viewsets.ModelViewSet):
  queryset = UserInfo.objects.all()
  serializer_class = UserInfoSerializer


#class user_detail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = UserInfo.objects.all()
#    serializer_class = UserInfoSerializer