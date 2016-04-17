from django.shortcuts import render
import sys
from django.http import HttpResponse

def index(request):
	return render(request, "data.html", {});

def dataInfo(request, dataId):
	return render(request, "dataInfo.html", {});


# Create your views here.
