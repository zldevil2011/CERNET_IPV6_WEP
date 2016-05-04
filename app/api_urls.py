from django.conf.urls import url, include
from rest_framework import routers
from app.api import auth 

router = routers.DefaultRouter()
router.register(r'users', auth.UserViewSet)
router.register(r'groups', auth.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
