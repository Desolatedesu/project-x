#!D:/Programs/Python/python.exe

import os, sys
import cgi, cgitb
from jinja import environment

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html\n')

template = environment.get_template('lab1.html')

message = ''
filepath = ''
file_content = ''
list = []
form = cgi.FieldStorage()

if "file" in form:
  filepath = str(form["file"].value)

  try:
    file = open(filepath,'r', encoding="utf-8")

    file_content = file.read()

    for word in file_content.split():
      if word[0].lower() in "eiuyo":
        list.append(word)
      else:
        continue

    file.close()
  except FileNotFoundError:
    message = 'File doesn\'t exist'
else:
  message = 'Enter a filename'

print(template.render(message=message, filename=filepath, file_content=file_content, list=list))
