# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app.models import News

from app.forms import UEditorTestModelForm,TestUEditorForm

def edit(request):
	if request.method == "POST":
		return HttpResponse("success")
	else:
		try:
			M=News.objects.get(pk=1)
			form = TestUEditorForm(instance= M)
		except Exception, e:
			print str(e)
			form = TestUEditorForm(
				initial={'content': '测试富文本编辑器'}
			)
		print "1234"
		print form
		# return render_to_response('test.html', {'form': form})
		return render(request, "adminer/editNews.html", {'form': form})

# Create your views here.
