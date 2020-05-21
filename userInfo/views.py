from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import UserInfo

# Create your views here.
class UserView(APIView):
    #POST /userInfo
    def post(self, request):
        userSerializer = UserSerializer(data=request.data)

        if userSerializer.is_valid():
            userSerializer.save()
            return Response(userSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #GET /user
    #GET /user/{userId}
    def get(self, request, **kwargs):
        if kwargs.get('userId') is None: #모든 User정보
            userQueryset = UserInfo.objects.all()
            userQueryset_serializer = UserSerializer(userQueryset, many = True)
            return Response(userQueryset_serializer.data, status=status.HTTP_200_OK)
        else: #특정 id 요청
            user_id = kwargs.get('userId')
            user_serializer = UserSerializer(UserInfo.objects.get(userId=user_id))
            return Response(user_serializer.data, status.HTTP_200_OK)

    #PUT /user/{userId}
    def put(self, request,**kwargs):
        if kwargs.get('userId'):
            if kwargs.get('userId') is None:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
            else:
                user_id = kwargs.get('userId')
                user_object = UserInfo.objects.get(userId= user_id)

                update_user_serializer = UserSerializer(user_object, data = request.data)
                if update_user_serializer.is_valid():
                    update_user_serializer.save()
                    return Response(update_user_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    #DELETE /user/{userId}
    def delete(self, request, **kwargs):
        if kwargs.get('userId') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get('userId')
            user_object = UserInfo.objects.get(userId=user_id)
            user_object.delete()
            return Response("Successful Delete", status=status.HTTP_200_OK)