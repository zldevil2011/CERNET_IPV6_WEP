from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(15*60)
def index(request):
	return render(request, "server/base.html", {});
# Create your views here.
