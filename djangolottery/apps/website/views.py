from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json
from models import Participants

def index(request):
	return render_to_response('website/index.html',{},context_instance=RequestContext(request))

def participate(request):
	name = request.POST['name']
	email = request.POST['email']
	bcaddress = request.POST['bcaddress']
	amount = request.POST['amount'].replace(',','.')

	try:
		participant = Participants(name=name, email=email, bcaddress=bcaddress, amount=amount)
		participant.save()
		status = {'status': 'ok'}
	except Exception as e:
		status = {'status': 'error'}

	return HttpResponse(json.dumps(status), content_type='application/json')
