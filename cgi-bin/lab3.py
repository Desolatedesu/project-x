#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

form = cgi.FieldStorage()

n = 0
list = []

a = str(form["x1"].value)
b = str(form["x2"].value)
c = str(form["x3"].value)

list.append(a)
list.append(b)
list.append(c)

for i, word in enumerate(list, start = 1):
	for letter in word:
		if letter.lower() in "aeouiyауеоюёяиэы":
			n++
		else:
			continue
	print("Строка " + str(i) + ": " + str(n) + " гласных букв.")
	n = 0
