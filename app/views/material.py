from django.shortcuts import render
import sys
from django.http import HttpResponse

def index(request):
	return render(request, "material.html", {});

def materialInfo(request, dataId):
	return render(request, "materialInfo.html", {});


# Create your views here.
