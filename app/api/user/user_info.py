# coding=utf-8
__author__ = 'hacker'
import logging
from rest_condition import Or
from rest_framework import status
from app.models import AppUser, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.ext.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from app.serializers import AppUserSerializer


class UserInfo(APIView):
    authentication_classes = [OAuth2Authentication, BasicAuthentication, SessionAuthentication,  ]
    permission_classes = (Or(IsAuthenticated, TokenHasScope,  ),)
    required_scopes = ['read','write']

    def get(self, request, format=None):
        user = request.user.appuser
        serializer = AppUserSerializer(user)
        return Response({'user':serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = request.user.appuser
        if request.data.get('nickname', None) != None:
            user.nickname = request.data['nickname']
        if request.data.get('phone', None) != None:
            user.phone = request.data['phone']
        if request.data.get('gender', None) != None:
            user.gender = request.data['gender']
        if request.data.get('age', None) != None:
            user.age = request.data['age']
        if request.data.get('location', None) != None:
            user.location = request.data['location']
        user.save()
        return Response(status=status.HTTP_200_OK)
