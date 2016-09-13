# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app.models import News
from django.views.decorators.csrf import csrf_exempt

from app.forms import UEditorTestModelForm,TestUEditorForm


def list(request):
	news_list = News.objects.all().order_by('-time')
	return render(request, "adminer/newsList.html", {
		"news_list": news_list,
	})


@csrf_exempt
def edit(request):
	print request.method
	if request.method == "POST":
		title = request.POST.get("title", None)
		content = request.POST.get("content", None)
		print title
		print content
		if title is None or content is None:
			return HttpResponse("error")
		try:
			news_id = request.POST.get("news_id", None)
			print "xx" + news_id + "yy"
			if news_id is None or news_id == "":
				print news_id
				news = News()
				news.title = title
				news.content = content
				news.author = "zhaolong"
				news.read_count = 0
				news.save()
			else:
				news = News.objects.get(news_id=int(news_id))
				news.title = title
				news.content = content
				news.author = "zhaolong"
				news.save()
			return HttpResponse("success")
		except:
			return HttpResponse("error")

	elif request.method == "GET":
		try:
			news_id = int(request.GET.get("nid", -1))
			news=News.objects.get(pk=news_id)
			form = UEditorTestModelForm(instance= news)
		except Exception, e:
			print str(e)
			form = TestUEditorForm( initial={'content': '请在此输入文字'} )
			news = None
		return render(request, "adminer/editNews.html", {
			'form': form,
			'news': news,
		})
	else:
		return HttpResponse("success")


def read(request, news_id):
	news_id = int(news_id)
	print news_id
	print type(news_id)
	if request.method == "POST":
		return HttpResponse("POST")
	else:
		try:
			news = News.objects.get(news_id=news_id)
			news.read_count += 1
			news.save()
		except News.DoesNotExist:
			return HttpResponse("不存在")

		return render(request, "adminer/news.html", {
			"news": news,
		})
# Create your views here.
