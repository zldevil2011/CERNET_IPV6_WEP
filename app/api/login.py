# -*- coding:utf-8 -*-
__author__ = 'hacker'
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import AppUser
from django.contrib.auth import authenticate
from wireless import settings
import requests
from oauth2_provider.models import Application

class Login(APIView):
	def post(self, request, format=None):
		username = request.data['username']
		password = request.data['password']
		user = authenticate(username = username, password = password)
		if user and user.is_active:
			app = settings.OAUTH_APPLICATION_NAME
			app = Application.objects.get(name = app)
			data = {
				'grant_type':'password',
				'username': username,
				'password': password,
				'client_id': app.client_id,
				'client_secret': app.client_secret,
			}
			url = settings.OAUTH2_GET_TOKEN_URL
			r = requests.post(url, data = (data))
			print app
			print data
			print r.json()
			return Response({'access_token':r.json()['access_token']}, status = status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_401_UNAUTHORIZED)
