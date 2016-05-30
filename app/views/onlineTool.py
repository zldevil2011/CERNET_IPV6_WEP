from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import Image

def handle_uploaded_file(f):
    try:
        # pass
        with open('./media/images/originalImage/' + unicode(f), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except Exception, e:
        print str(e)


def imageProcessing(filename, postfix):
	path = "./media/images/originalImage/" + filename + "." + postfix
	im = Image.open(path)
	pix = im.load()
	width = im.size[0]
	height = im.size[1]
	for i in range(width):
		for j in range(height):
			t = (float)(pix[i,j][1] - pix[i,j][0]) / (float)(pix[i,j][1] + pix[i,j][0])
			if t > 0.03 or (pix[i,j][0] > 250 and pix[i,j][1] >250 and pix[i,j][2] >250):
				pix[i,j] = (255,255,255)
			else:
				pix[i,j] = (0,0,0)
	im.save("./media/images/processImage/" + filename + ".bmp" ,"BMP")


def index(request):
	return render(request, "onlineTool.html", {})


def calculator(request, id):
	return render(request, "toolWindow.html", {})


@csrf_exempt
def upload(request):
	original_image = request.FILES.getlist('originalImage')
	print original_image
	thumbnailStr = ""
	for file in original_image:
		handle_uploaded_file(file)
		thumbnailStr = unicode(file)

	print '11111111111111111111111111111111111111111111111111'
	print thumbnailStr
	return HttpResponse(thumbnailStr)


@csrf_exempt
def transfer(request):
	print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	file = request.POST.get("originalFile", None)
	try:
		filename = file.split('.')[0]
		postfix = file.split('.')[1]
		imageProcessing(filename, postfix)
	except Exception, e:
		print str(e)
	return HttpResponse(filename + ".bmp")



# if __name__ == "__main__":
# 	imageProcessing("xxx")

# Create your views here.
