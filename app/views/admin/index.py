# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app.models import News

from app.forms import UEditorTestModelForm,TestUEditorForm

def index(request):
	if request.method == "POST":
		return HttpResponse("success")
	else:
		return render(request, "adminer/index.html", {})

# Create your views here.
