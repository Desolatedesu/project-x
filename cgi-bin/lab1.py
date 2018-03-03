#!D:/Programs/Python/python.exe

import os, sys
import cgi, cgitb
from jinja import environment

cgitb.enable()
sys.stderr = sys.stdout

template = environment.get_template('lab1.html')

form = cgi.FieldStorage()
list = []

# filepath = str(form["x1"].value)
# file = open('filepath','r', encoding="utf-8")
file = open('./azaza','r', encoding="utf-8")

file_content = file.read()

for word in file_content.split():
	if word[0].lower() in "eiuyo":
		list.append(word)
	else:
		continue

file.close()

print('Content-type: text/html\n')
print(template.render(file_content=file_content, list=list))
