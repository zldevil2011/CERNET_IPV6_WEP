# -*- coding:utf-8 -*-
from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from app.models import Air, Forecast
import datetime


@cache_page(15*60)
def index(request):
	location='北京'
	weekArr = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六","星期天"]
	latest = Air.objects.filter(location=location).order_by('-time')[0]
	today = datetime.date.today()
	week = weekArr[today.weekday()]
	print latest
	forecast = Forecast.objects.filter(location=location).order_by('date')
	print forecast
	for fore in forecast:
		fore.week = weekArr[int(fore.week)]
	return render(request, "index.html", {
		"latest": latest,
		"week": week,
		"forecast": forecast
	})
# Create your views here.
