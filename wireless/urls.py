"""wireless URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
import settings
import video
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^ueditor/',include('DjangoUeditor.urls' )),
	url(r'',include('app.urls')),
	url(r'^api/',include('app.api_urls')),
	url(r'^adminxl/',include('app.admin_urls')),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	url(r'^web_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
	url(r'^video/', video.video)
	#url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	
]
