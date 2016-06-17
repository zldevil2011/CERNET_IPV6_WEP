from django.contrib.auth.models import User, Group
from app.models import AppUser,Air, Forecast
from rest_framework import serializers


class AppUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = AppUser
		fidlds = ('id', 'sex', 'nickname', 'portrait', 'email', 'register_date', 'phone', 'location')

class AirSerializer(serializers.ModelSerializer):
	class Meta:
		model = Air
		fields = ('air_id', 'aqi', 'pm25', 'temperature', 'high_temperature', 'low_temperature', 'humidity', 'cloud',
				  'cloud_speed', 'weather', 'location', 'date', 'time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

