from django.conf.urls import url, patterns, include
import views.index
import views.data

urlpatterns = [
	url('^$', views.index.index, name="index"),
	url('^data$', views.data.index, name="data_index"),
	url('^imageInfo$', views.data.imageInfo, name="imageInfo"),
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
]
