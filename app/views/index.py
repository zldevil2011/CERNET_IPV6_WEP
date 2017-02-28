# -*- coding:utf-8 -*-
from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.core.cache import cache
from django.core import serializers
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from app.models import Air, Forecast
import datetime
import json
weekArr = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六","星期天"]
@cache_page(15*60)
def index(request):
	try:
		location='北京'
		latest = Air.objects.filter(location=location).order_by('-date', '-time')[0]
		all_city_air = Air.objects.all()
		city_list = []
		for city in all_city_air:
			city_list.append(city.location)

		today = datetime.date.today()
		week = weekArr[today.weekday()]
		print latest
		forecast = Forecast.objects.filter(location=location).order_by('date')[0:6]
		print forecast
		for fore in forecast:
			fore.week = weekArr[int(fore.week)]
	except:
		latest = None
		week = None
		forecast = None
		city_list = None
	return render(request, "index.html", {
		"latest": latest,
		"week": week,
		"forecast": forecast,
		"city_list": city_list
	})

@csrf_exempt
def location_city_all_info(request):
	location = request.POST.get("location", "北京")
	latest = Air.objects.filter(location=location).order_by('date').order_by('-time')[0]
	city_data = []
	latest_dic = {}
	latest_dic["air_id"] = latest.air_id
	latest_dic["aqi"] = latest.aqi
	latest_dic["pm25"] = latest.pm25
	latest_dic["temperature"] = latest.temperature
	latest_dic["high_temperature"] = latest.high_temperature
	latest_dic["low_temperature"] = latest.low_temperature
	latest_dic["humidity"] = latest.humidity
	latest_dic["cloud"] = latest.cloud
	latest_dic["cloud_speed"] = latest.cloud_speed
	latest_dic["weather"] = latest.weather
	latest_dic["location"] = latest.location
	latest_dic["date"] = latest.date
	latest_dic["time"] = latest.time

	forecast_querySet = Forecast.objects.filter(location=location).order_by('date')[0:6]
	forecast_list = []
	for forecast in forecast_querySet:
		forecast.week = weekArr[int(forecast.week)]
		forecast_dic = {}
		forecast_dic["forecast_id"] = forecast.forecast_id
		forecast_dic["location"] = forecast.location
		forecast_dic["date"] = forecast.date
		forecast_dic["week"] = forecast.week
		forecast_dic["weather_day"] = forecast.weather_day
		forecast_dic["weather_night"] = forecast.weather_night
		forecast_dic["high_temperature"] = forecast.high_temperature
		forecast_dic["low_temperature"] = forecast.low_temperature
		forecast_dic["cloud"] = forecast.cloud
		forecast_dic["cloud_speed"] = forecast.cloud_speed
		forecast_dic["aqi"] = forecast.aqi
		forecast_dic["status"] = forecast.status
		forecast_list.append(forecast_dic)
	city_data.append(latest_dic)
	city_data.append(forecast_list)
 	return HttpResponse(json.dumps(city_data), "application/json")

# Create your views here.
