from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json

def index(request):
	return render_to_response('website/index.html',{},context_instance=RequestContext(request))

def participate(request):
	data = {
		'works': 'yes'
	}

	name = request.POST['name']
	email = request.POST['email']
	bcaddress = request.POST['bcaddress']
	amount = request.POST['amount']

	return HttpResponse(json.dumps(data), content_type='application/json')
