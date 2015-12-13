from django.shortcuts import render
from django.http import HttpResponse
from mysite.settings import *

def hello(request):
	return render(request,'hello.html')

def histogram(request,filename):
	try:
		fileroot = os.path.join(os.path.dirname(BASE_DIR),"static","templates",filename)
		opened = open(fileroot)
		hist = {}   # dictionary for histogram.
		for word in opened.read().split(" "):
			hist.setdefault(word,0)
			hist[word] += 1
		result = "<strong>Name:</strong> %s </br><strong>Words:</strong></br>" %filename
		for word in hist:
			result += "%s : %d </br>" %(word, hist[word])
		return HttpResponse(result)
	except:
		return HttpResponse('There is no such a file.')




