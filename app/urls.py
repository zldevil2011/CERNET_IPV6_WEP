from django.conf.urls import url, patterns, include
import views.index
import views.data
import views.products
import views.material
urlpatterns = [
	url('^$', views.index.index, name="index"),
	url('^data$', views.data.index, name="data_index"),
	url('^dataInfo/(\d+)/$', views.data.dataInfo, name="dataInfo"),
	url('^products/$', views.products.index, name="products_index"),
	url('^productInfo/(\d+)/$', views.products.productInfo, name="productInfo"),
	url('^material/$', views.material.index, name="material_index"),
	url('^productInfo/(\d+)/$', views.material.materialInfo, name="materialInfo"),
#     # url('^welcome/$', views.welcome.welcome(), name="welcome"),
]
