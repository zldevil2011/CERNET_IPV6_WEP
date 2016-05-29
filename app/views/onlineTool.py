from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time

def index(request):
	return render(request, "onlineTool.html", {})


def calculator(request, id):
	return render(request, "toolWindow.html", {})


@csrf_exempt
def upload(request):
	original_image = request.FILES.getlist('originalImage')
	print original_image
	print '11111111111111111111111111111111111111111111111111'
	return HttpResponse("success")


@csrf_exempt
def transfer(request):
	print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	print request.POST
	# time.sleep(500)
	return HttpResponse("success")
# Create your views here.
