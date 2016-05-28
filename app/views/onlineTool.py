from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return render(request, "onlineTool.html", {})


def calculator(request, id):
	return render(request, "toolWindow.html", {})


@csrf_exempt
def upload(request):
	print '11111111111111111111111111111111111111111111111111'
	return HttpResponse("success")
# Create your views here.
