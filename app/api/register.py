#coding=utf-8
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from django.core.mail import send_mail
from django.core.cache import cache
from app.models import User, AppUser
import datetime
from wireless import settings
from django.views.decorators.csrf import csrf_exempt


class SendMail(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        '''
        发送邮件
        :param email:邮件名
        :return:403,发送失败
                200,发送成功
        '''
        print "okokoko"
        code = random.randint(1000, 9999)
        subject = 'wireless code'
        from_email = settings.EMAIL_HOST_USER
        to = request.data['email']
        text_content = 'Your code is%s,please check it within 30mins！'%code
        print "begin--"
        print request 
        print "end--"
        try:
            send_mail(subject, text_content, from_email, [to], fail_silently=False)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)
        print to + 'code'
        cache.set(to+'code', code, 1800)
        print cache.get(to+'code')
        return Response(status=status.HTTP_200_OK)


class CheckCode(APIView):

    def post(self, request, format=None):
        '''
        验证邮箱验证码是否正确
        :param email:邮箱
        :param code:验证码
        :return: 404,验证码错误
                 200,验证码正确
        '''
        email = request.data['email']
        code = request.data['code']
        code1 = cache.get(email+'code')
        if code1 is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if int(code1) != int(code):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)


class Register(APIView):
    def post(self, requests, format=None):
        '''
        注册,验证码成功之后进行注册
        :param username:用户名
        :param password: 密码
        :return: 201,注册成功
        '''
        username = requests.data['username']
        password = requests.data['password']
        try:
            user = User.objects.get(username=username)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            user = User.objects.create_user(username=username, password=password,
                                            last_login=datetime.datetime.now(), email=username)
            user.save()
            appuser = AppUser()
            appuser.user = user
            appuser.save()
            return Response(status=status.HTTP_201_CREATED)
