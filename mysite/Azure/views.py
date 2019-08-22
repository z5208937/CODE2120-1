from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *

# Create your views here.

def example_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def fib(request):
	jsob ={"startNumber": 0, "length": 10} #Defaults
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			###################################
			## CUSTOM FUNCTION BELOW ##########
			###################################
			
			startNumber = int(jsob["startNumber"])
			length      = int(jsob["length"])
			loop	    = range(length)
			numarray    = []
			fibno 		= startNumber
			addno 		= 1
			for l in loop:
				numarray.append(fibno)
				fibno = fibno+addno
				addno = fibno-addno

			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")

@csrf_exempt
def add(request):
	jsob ={"NumberA": input, "NumberB": input} #Defaults
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			NumberA = int(jsob["NumberA"])
			NumberB = int(jsob["NumberB"])

			Answer = NumberA + NumberB

			return JsonResponse({"add": Answer})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")
