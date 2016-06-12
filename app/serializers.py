from django.contrib.auth.models import User, Group
from app.models import AppUser
from rest_framework import serializers


class AppUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = AppUser
		fidlds = ('id', 'sex', 'nickname', 'portrait', 'email', 'register_date', 'phone', 'location')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

