# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app.models import News
from django.views.decorators.csrf import csrf_exempt

from app.forms import UEditorTestModelForm,TestUEditorForm


@csrf_exempt
def edit(request):
	if request.method == "POST":
		title = request.POST.get("title", None)
		content = request.POST.get("content", None)
		print title
		print content
		if title is None or content is None:
			return HttpResponse("error")
		print "yyyy"
		news = News()
		news.title = title
		news.content = content
		news.author = "zhaolong"
		news.read_count = 0
		news.save()
		print "xxxx"
		return HttpResponse("success")
	else:
		try:
			M=News.objects.get(pk=-1)
			form = UEditorTestModelForm(instance= M)
		except Exception, e:
			print str(e)
			form = TestUEditorForm(
				initial={'content': '请在此输入文字'}
			)
		# print "1234"
		# print form
		# return render_to_response('test.html', {'form': form})

		return render(request, "adminer/editNews.html", {
			'form': form,
			# 'content': M.content,
		})

# Create your views here.
