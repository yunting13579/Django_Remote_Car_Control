# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
# from dwebsocket import require_websocket,accept_websocket
# import dwebsocket
import json
import time
import random
from trips.models import GPS_data

car_status = 'stop'
GPS_data_count = 0
servo1 = 0
servo2 = 0
servo3 = 0
servo4 = 0
servo5 = 0
servo6 = 0
# json_data = {'status': car_status,
# 			 'servo1': servo1,
# 			 'servo2': servo2,
# 			 'servo3': servo3,
# 			 'servo4': servo4,
# 			 'servo5': servo5,
# 			 'servo6': servo6}

def index(request):
	return redirect('/home/')

#html page response
def home_page(request):
	gps = GPS_data.objects.order_by('-id')[0]
	return render(request,'trips/home.html',{'latest':gps})
	#return render(request,'home.html')

def GPS_Sheet(request):
	global GPS_data_count
	GPS_data_count = GPS_data.objects.all().count()
	gps = GPS_data.objects.all()
	return render(request,'trips/GPS_Sheet.html',{'gps_sheet':gps})

def robotic_arm(request):
	global servo1,servo2,servo3,servo4,servo5,servo6
	# global json_data
	return render(request, 'trips/robotic_arm.html', {'servo1': servo1,
														'servo2': servo2,
														'servo3': servo3,
														'servo4': servo4,
														'servo5': servo5,
														'servo6': servo6})

def GPS_Sheet_update(request):
	count = GPS_data.objects.all().count()
	if count > GPS_data_count:
		gps = GPS_data.objects.filter(id=count-1)
		json = {'datetime':gps.datetime,'lat':gps.latitude,'lng':gps.longitude}
	return JsonResponse(json,safe=False)

def sent_data(request):
	count = GPS_data.objects.all().count()
	gps = GPS_data.objects.order_by('-id')[0]
	print(gps.datetime,gps.latitude,gps.longitude)
	gps_json = {'datetime':gps.datetime,'lat':gps.latitude,'lng':gps.longitude}
	
	return JsonResponse(gps_json,safe=False)

#receive data from /send_django
def recieve_data(request):
	data1 = request.GET.get('status')
	global car_status
	car_status = data1
	#print(car_status)
	return JsonResponse({'status':'success'}, safe=False)

#send data to /pi_car for autocar
def car_data(request):
	global servo1,servo2,servo3,servo4,servo5,servo6,car_status
	car_json = {'status': car_status,
			 'servo1': servo1,
			 'servo2': servo2,
			 'servo3': servo3,
			 'servo4': servo4,
			 'servo5': servo5,
			 'servo6': servo6}
	return JsonResponse(car_json, safe=False)

#receive robotic_arm value from web
def robotic_arm_value(request):
	global servo1,servo2,servo3,servo4,servo5,servo6
	servo1 = request.GET.get('servo1')
	servo2 = request.GET.get('servo2')
	servo3 = request.GET.get('servo3')
	servo4 = request.GET.get('servo4')
	servo5 = request.GET.get('servo5')
	servo6 = request.GET.get('servo6')

	print('servo1:',servo1,'servo2:',servo2,'servo3:',servo3,
		  'servo4:', servo4,'servo5:',servo5,'servo6:',servo6)
	return JsonResponse({'status': 'success'}, safe=False)
