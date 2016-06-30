from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.



def index(request):
	 
    y = {}

    return render_to_response('index.html',y)

def travel(request):
	 
    y = {}

    return render_to_response('travel\gokarna.html',y)