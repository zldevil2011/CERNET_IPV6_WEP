# coding:utf-8
from django.conf.urls import url, patterns, include
from django.views.generic import TemplateView
import views.admin.news

urlpatterns = [
	url('^editNews$', views.admin.news.edit, name="editNews"),
]
