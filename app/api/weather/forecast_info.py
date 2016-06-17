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
from app.serializers import ForecastSerializer
from app.models import Forecast


class ForecastInfo(APIView):
    authentication_classes = [OAuth2Authentication, BasicAuthentication, SessionAuthentication,  ]
    permission_classes = (Or(IsAuthenticated, TokenHasScope,  ),)
    required_scopes = ['read', 'write']

    def get(self, request, format=None):
        location = request.GET.get('location', '北京')
        try:
            item = Forecast.objects.get(location=location)
        except Forecast.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ForecastSerializer(item)
        return Response({'air':serializer.data}, status=status.HTTP_200_OK)


