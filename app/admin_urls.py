# coding:utf-8
from django.conf.urls import url, patterns, include
from django.views.generic import TemplateView
import views.admin.index

urlpatterns = [
	url('^$', views.admin.index.index, name="wsn_index"),
]
