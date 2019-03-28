#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import django
sys.path.append('/home/pi/myvenv/mysite') # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' # 设置项目的配置文件
django.setup() # 加载项目配置

import paho.mqtt.client as mqtt
import sqlite3
import datetime
from trips.models import GPS_data

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("test")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	#get sys time
	ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
	theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
	#split message
	mqtt_data = str(msg.payload)
	temp = mqtt_data.split(',')
	lat = temp[0]
	lng = temp[1]
	#insert data to db.sqlite3
	b = GPS_data(datetime=theTime,latitude=str(lat),longitude=str(lng))
	b.save()
	print("Records created successfully")
if __name__ == "__main__":
	try:
		client = mqtt.Client()
		client.username_pw_set("yunting", "user1325")
		client.on_connect = on_connect
		client.on_message = on_message
		client.connect("140.134.31.153", 1883, 60)
		client.loop_forever()
	except KeyboardInterrupt:
		print("連線關閉")
