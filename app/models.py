#coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# 用户信息
class AppUser(models.Model):
	user = models.OneToOneField(User)
	sex = models.IntegerField(default = 0)
	nickname = models.CharField(max_length = 30)
	portrait = models.CharField(max_length = 200, null = True)
	email = models.EmailField(null=True)
	register_date = models.DateField(auto_now_add = True)
	phone = models.CharField(max_length=20, null=True)
	location = models.CharField(max_length = 100, null = True)

	def __unicode__(self):
		return str(self.id)


#管理员信息
class Admin(models.Model):
	admin_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	priority = models.IntegerField(default = 0)

	def __unicode__(self):
		return str(self.username)


# 空气质量
class Air(models.Model):
	air_id = models.AutoField(primary_key = True)
	aqi = models.IntegerField(default = 0, null = True)
	pm25 = models.CharField(max_length=200, null = True)
	temperature = models.FloatField(default = 0, null = True)
	high_temperature = models.FloatField(default= 0, null=True)
	low_temperature = models.FloatField(default= 0,  null=True)
	humidity = models.FloatField(default = 0, null = True)
	cloud = models.CharField(max_length=200, null = True)
	cloud_speed = models.FloatField(default = 0, null = True)
	weather = models.CharField(max_length=200, null = True)
	location = models.CharField(max_length = 200, null = True)
	date = models.CharField(max_length=200, null=True)
	time = models.CharField(max_length=200, null=True)
	
	def __unicode__(self):
		return str(self.air_id)


# 预报
class Forecast(models.Model):
	forecast_id = models.AutoField(primary_key = True)
	location = models.CharField(max_length = 200, null = True)
	date = models.CharField(max_length = 200, null=True)
	week = models.CharField(max_length = 200, null = True)
	weather_day = models.CharField(max_length = 200, null = True)
	weather_night = models.CharField(max_length = 200, null = True)
	high_temperature = models.FloatField(default = 0.0)
	low_temperature = models.FloatField(default = 0.0)
	cloud = models.CharField(max_length = 200, null = True)
	cloud_speed = models.CharField(max_length=200, null=True)
	aqi = models.IntegerField(default = 0)
	status = models.CharField(max_length = 100, null = True)
	
	def __unicode__(self):
		return str(self.forecast_id)

# 云图
class Nephogram(models.Model):
	nephogram_id = models.AutoField(primary_key = True)
	classification = models.CharField(max_length=200, null = True)
	title = models.CharField(max_length = 200, null = True)
	image_path = models.CharField(max_length = 300, null = True)

	def __unicode__(self):
		return str(self.nephogram_id)


# news
class News(models.Model):
	news_id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=200, null = True)
	content = models.TextField(null = True)
	author = models.CharField(max_length = 200, null = True)
	time = models.DateTimeField(auto_now_add = True)
	read_count = models.IntegerField(default = 0, null = True)
	
	def __unicode__(self):
		return str(self.news_id)


# Create your models here.
