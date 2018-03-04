#!D:/Programs/Python/python.exe

import os,sys
import cgi, cgitb
from jinja import environment

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html\n')

template = environment.get_template('lab2.html')

form = cgi.FieldStorage()
message = ''
result = ''

if "x" in form and "y" in form and "z" in form:
  x = int(form["x"].value)
  y = int(form["y"].value)
  z = int(form["z"].value)

  rang = range(y, z)

  if x in rang:
    result = "Число {} принадлежит промежутку [{};{}]".format(x,y,z)
  else:
    result = "Число {} не принадлежит промежутку [{};{}]".format(x,y,z)
else:
  message = 'Введите данные'

print(template.render(message=message, result=result))
