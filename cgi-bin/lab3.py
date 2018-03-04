#!D:/Programs/Python/python.exe

import os,sys
import cgi, cgitb
from jinja import environment

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html\n')

template = environment.get_template('lab3.html')

form = cgi.FieldStorage()
message = ''
result = ''
n = 0
list = []

if "x" in form and "y" in form and "z" in form:
  list.append(str(form["x"].value))
  list.append(str(form["y"].value))
  list.append(str(form["z"].value))

  for i, word in enumerate(list, start = 1):
    for letter in word:
      if letter.lower() in "aeouiyауеоюёяиэы":
        n = n + 1
    result += "Строка " + str(i) + ": " + str(n) + " гласных букв, "
    n = 0
else:
  message = 'Введите данные'

print(template.render(message=message, result=result))
