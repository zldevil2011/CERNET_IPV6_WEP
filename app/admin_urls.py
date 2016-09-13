# coding:utf-8
from django.conf.urls import url, patterns, include
from django.views.generic import TemplateView
import views.admin.index
import views.admin.news
import views.admin.data

urlpatterns = [
	url('^$', views.admin.index.index, name="admin_index"),
	url('^index/$', views.admin.index.index, name="admin_index"),
	url('^data/$', views.admin.data.index, name="admin_data"),
	url('^news/edit/$', views.admin.news.edit, name="editNews"),
	url('^news/(?P<news_id>\d+)/$', views.admin.news.read, name="readNews"),
]
