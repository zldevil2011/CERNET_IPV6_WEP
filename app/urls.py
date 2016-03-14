from django.conf.urls import url, patterns, include
import views.index

urlpatterns = [
	url('^$', views.index.index, name="index"),
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
]
