# -*- encoding=utf-8 -*-
__author__ = 'hacker'
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from django.core.mail import send_mail
from django.core.cache import cache
from app.models import AppUser
from django.contrib.auth import authenticate
from wireless import settings
from oauth2_provider.models import Application
import datetime

class SendMail(APIView):
	def post(self, request, format=None):
		code = random.randint(1000, 9999)
		subject = 'wireless Email Checked'
		from_email = settings.EMAIL_HOST_USER
		to = request.data['email']
		text_content = "Your code is %s, Please check it within 30mins" % code
		
		try:
			send_mail(subject, text_content, from_email, [to], fail_silently=False)
		except:
			return Response(status=status.HTTP_403_FORBIDDEN)
		
		 
