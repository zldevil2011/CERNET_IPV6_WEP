from django.shortcuts import render
import sys
from django.http import HttpResponse

def index(request):
	return render(request, "products.html", {});

def productInfo(request, dataId):
	return render(request, "productInfo.html", {});


# Create your views here.
