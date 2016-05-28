# coding:utf-8
from django.conf.urls import url, patterns, include
from django.views.generic import TemplateView
import views.index
import views.data
import views.products
import views.material
import views.onlineTool
import views.server.index

urlpatterns = [
	url('^$', views.server.index.index, name="index"),
	url('^home/$', views.index.index, name="wsn_index"),
	url('^data/$', views.data.index, name="data_index"),
	url('^dataInfo/(\d+)/$', views.data.dataInfo, name="dataInfo"),
	url('^products/$', views.products.index, name="products_index"),
	url('^productInfo/(\d+)/$', views.products.productInfo, name="productInfo"),
	url('^material/$', views.material.index, name="material_index"),
	url('^productInfo/(\d+)/$', views.material.materialInfo, name="materialInfo"),
	url('^nephogram/$', TemplateView.as_view(template_name="nephogram.html")),
	url('^onlineTool/$', views.onlineTool.index, name="onlineTool"),
	url('^onlineTool/(\d+)/$', views.onlineTool.calculator, name="onlineTool"),
	url('^onlineTool/upload/$', views.onlineTool.upload, name="upload"),
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
]
