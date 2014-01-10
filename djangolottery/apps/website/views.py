from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
	return render_to_response('website/index.html',{},context_instance=RequestContext(request))

def draw(request):
	return render_to_response('website/draw.html',{},context_instance=RequestContext(request))
