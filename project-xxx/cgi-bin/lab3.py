#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
from math import *

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html;charset=windows-1251\n')

with open('../public_html/header.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

form = cgi.FieldStorage()

if "number" in form:
  a = int(form.getvalue('number'))

  print("<p>Введённое число <b>")
  if a > 0: print("положительное")
  if a < 0: print("отрицательное")
  if a == 0: print("ноль")
  print("</b></p>")

with open('../public_html/lab3.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

with open('../public_html/footer.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)
