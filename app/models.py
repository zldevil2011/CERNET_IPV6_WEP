#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

#用户信息
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
	pm25 = model.IntegerField(default = 0, null = True)
	temperature = model.FloatField(default = 0, null = True)
	humidity = model.FloatField(default = 0, null = True)
	cloud = models.CharField(max_length=200, null = True)
	cloud_speed = model.FloatField(default = 0, null = True)
	weather = model.CharField(max_length=200, null = True)

	def __unicode__(self):
		return str(self.air_id)

# Create your models here.
