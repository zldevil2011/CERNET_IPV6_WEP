#coding:utf-8
from __future__ import unicode_literals

from django.db import models

#用户信息
class User(models.Model):
	user_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.user_id


#管理员信息
class Admin(models.Model):
	admin_id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	priority = models.IntegerField()

	def __unicode__(self):
		return self.username	
# Create your models here.
