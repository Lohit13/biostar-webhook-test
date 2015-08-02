from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import constant_time_compare
import json, hmac, base64, hashlib

def verify(ip):
	ip = ip.split('.')
	if ip[0]=='192' and ip[1]=='30':
		if int(ip[2])>=252 and int(ip[2])<=255:
			if int(ip[3])>=0 and int(ip[3])<=255:
				return True
			else:
				return False
		else:
			return False
	else:
		return False


@csrf_exempt
def webhookupdate(request):
	if request.META.get('CONTENT_TYPE') == 'application/json':
		if verify(request.META.get('REMOTE_ADDR')):
			cmd = settings.BASE_DIR+"/update.sh"
			os.system('%s'%(cmd))
			return HttpResponse("All done!")
		else:
			raise Http404
	else:
		raise Http404
