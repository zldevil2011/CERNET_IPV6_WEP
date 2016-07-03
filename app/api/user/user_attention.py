# coding=utf-8
__author__ = 'hacker'
import logging
from rest_condition import Or
from rest_framework import status
from app.models import AppUser, User, Air, Forecast
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.ext.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from app.serializers import AppUserSerializer, AirSerializer, ForecastSerializer
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class UserAttention(APIView):
    authentication_classes = [OAuth2Authentication, BasicAuthentication, SessionAuthentication,  ]
    permission_classes = (Or(IsAuthenticated, TokenHasScope,  ),)
    required_scopes = ['read','write']

    def get(self, request, format=None):
        user = request.user.appuser
        print user.location
        attention_location_list = user.location.split(';')
        attention_info_list = []
        for location in attention_location_list:
            dic_tmp = {}
            dic_tmp["location"] = location
            air = Air.objects.filter(location=location).order_by('-date', '-time')[0]
            forecast = Forecast.objects.filter(location=location)
            dic_tmp["air"] = AirSerializer(air).data
            dic_tmp["forecast"] = ForecastSerializer(forecast, many=True).data
            attention_info_list.append(dic_tmp)
        return Response({'attention_info_list': attention_info_list}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = request.user.appuser
        if request.data.get('location', None) != None:
            user.location = user.location + ";" + request.data['location']
        user.save()
        return Response(status=status.HTTP_200_OK)
