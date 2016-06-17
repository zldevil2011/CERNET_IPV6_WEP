from django.conf.urls import url, include

from app.api.register import SendMail, CheckCode, Register
from app.api.user.login import Login
from app.api.user.user_info import UserInfo
from app.api.weather.air_info import AirInfo
#router = routers.DefaultRouter()
#router.register(r'users', auth.UserViewSet)
#router.register(r'groups', auth.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	#url(r'^', include(router.urls)),
	url(r'^send_mail/', SendMail.as_view()),
	url(r'^check_code/', CheckCode.as_view()),
	url(r'^register/', Register.as_view()),
	url(r'^login/', Login.as_view()),
	url(r'^user_info/', UserInfo.as_view()),
	url(r'^air_info/', AirInfo.as_view()),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
