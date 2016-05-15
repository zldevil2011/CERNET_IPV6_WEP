from django.contrib import admin
from models import Admin, AppUser, Air, Forecast, Nephogram, News

class AdminAdmin(admin.ModelAdmin):
	list_display = ('admin_id', 'username')

class AppUserAdmin(admin.ModelAdmin):
	list_display = ('id', 'nickname', 'email')

class AirAdmin(admin.ModelAdmin):
	list_display = ('air_id', 'location', 'location', 'date', 'time')

class ForecastAdmin(admin.ModelAdmin):
	list_display = ('forecast_id', 'date', 'aqi')

class NephogramAdmin(admin.ModelAdmin):
	list_display = ('nephogram_id', 'title')

class NewsAdmin(admin.ModelAdmin):
	list_display = ('news_id', 'title')

admin.site.register(Admin, AdminAdmin)
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Air, AirAdmin)
admin.site.register(Forecast, ForecastAdmin)
admin.site.register(Nephogram, NephogramAdmin)
admin.site.register(News, NewsAdmin)
# Register your models here.
