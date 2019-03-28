#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import datetime

lat = 24.1234
lng = 120.2234
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
print "Opened database successfully";

#get sys time
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
#insert data to db.sqlite3
c.execute("INSERT INTO trips_gps_data values (?,?,?,?)",(0,theTime,str(lat),str(lng)))
conn.commit()
print "Records created successfully";
conn.close()
