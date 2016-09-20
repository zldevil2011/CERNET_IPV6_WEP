from django.shortcuts import HttpResponse, render


def video(request):
	return render(request, "video.html", {})