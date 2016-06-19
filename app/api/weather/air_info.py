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
from app.serializers import AirSerializer
from app.models import Air


class AirInfo(APIView):
    # authentication_classes = [OAuth2Authentication, BasicAuthentication, SessionAuthentication,  ]
    # permission_classes = (Or(IsAuthenticated, TokenHasScope,  ),)
    # required_scopes = ['read', 'write']

    def get(self, request, format=None):
        location = unicode(request.GET.get('location', '北京'))
        print "xxx"
        print location
        print "yyy"
        try:
            item = Air.objects.filter(location=location).order_by('-time')[0]
        except Air.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AirSerializer(item)
        return Response({'air':serializer.data}, status=status.HTTP_200_OK)


