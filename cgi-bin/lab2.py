#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

form = cgi.FieldStorage()

x = int(form["x"].value)
y = int(form["y"].value)
z = int(form["z"].value)

rang = range(y, z)

if x in rang:
	print("Число {} принадлежит промежутку [{};{}]".format(x,y,z))
else:
	print("Число {} не принадлежит промежутку [{};{}]".format(x,y,z))