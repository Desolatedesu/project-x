#!/usr/bin/env python3.4

import os, sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

form = cgi.FieldStorage()
list = []

filepath = str(form["x1"].value)
file = open(filepath,'r', encoding="utf-8")

print("Исходный текст:\n")
print(f.read())
print("_" * 100 + "\n")

for word in file.read().split(' '):
	if word[0].lower() == 'a' or word[0].lower() == 'e' or word[0].lower() == 'i' or word[0].lower() == 'u' or word[0].lower() == 'y' or word[0].lower() == 'o':
		list.append(word)
	else:
		continue

for right in list:
	print(right)

file.close()
