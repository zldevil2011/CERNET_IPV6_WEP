from django.shortcuts import render
import sys
from django.http import HttpResponse

def index(request):
	return render(request, "data.html", {});

def imageInfo(request):
	return render(request, "imageInfo.html", {});


# Create your views here.
