from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json
from djangolottery.apps.website.models import Participants

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

def draw(request):
	result = {'status': 'ok'}
	return HttpResponse(json.dumps(result), content_type='application/json')