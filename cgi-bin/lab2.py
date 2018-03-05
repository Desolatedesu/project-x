#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html\n')

with open('../public_html/header.html', mode='r') as file_read:
  for line in file_read:
    print(line)

form = cgi.FieldStorage()

if "x" in form and "y" in form and "z" in form:
  x = int(form["x"].value)
  y = int(form["y"].value)
  z = int(form["z"].value)

  rang = range(y, z)

  print('<h2>Results:</h2>')
  if x in rang:
    print("<p>Число {} принадлежит промежутку [{};{}]</p>".format(x,y,z))
  else:
    print("<p>Число {} не принадлежит промежутку [{};{}]</p>".format(x,y,z))
else:
  print('<div class="error">Введите данные</div>')

with open('../public_html/lab2.html', mode='r') as file_read:
  for line in file_read:
    print(line)

with open('../public_html/footer.html', mode='r') as file_read:
  for line in file_read:
    print(line)
