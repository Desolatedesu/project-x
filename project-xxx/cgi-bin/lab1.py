#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
import math

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html;charset=windows-1251\n')

with open('../public_html/header.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

form = cgi.FieldStorage()

if "a" in form and "h" in form and "r" in form and "r" in form:
  A = float(form["r"].value)
  H = float(form["h"].value)
  R = float(form["r"].value)
  M = float(form["v"].value)
  print("<p>")
  if M <= A**3 and M <= math.pi * R**2 * H:
    print ("Жидкость с данным объемом поместится в обе ёмкости")
  elif M <= A**3:
    print ("Жидкость с данным объемом поместится в кубическую ёмкость")
  elif M <= math.pi * R**2 * H:
    print ("Жидкость с данным объемом поместится в цилиндрическую ёмкость")
  else:
    print ("Жидкость с данным объемом не поместится ни в одну ёмкость")
  print("</p>")

with open('../public_html/lab1.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

with open('../public_html/footer.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)
