from django.shortcuts import render
import sys
from django.http import HttpResponse


def index(request):
	return render(request, "onlineTool.html", {})


def calculator(request, id):
	return render(request, "toolWindow.html", {})

# Create your views here.
