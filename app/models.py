#coding:utf-8
from __future__ import unicode_literals

from django.db import models

#用户信息
class AppUser(models.Model):
	user_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	sex = models.IntegerField(default = 0)
	nickname = models.CharField(max_length = 30)
	portrait = models.CharField(max_length = 200, null = True)
	email = models.EmailField(null=True)
	register_date = models.DateField(auto_now_add = True)
	phone = models.CharField(max_length=20, null=True)
	location = models.CharField(max_length = 100, null = True)
	
	def __unicode__(self):
		return str(self.username)


#管理员信息
class Admin(models.Model):
	admin_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	priority = models.IntegerField(default = 0)

	def __unicode__(self):
		return str(self.username)
# Create your models here.
