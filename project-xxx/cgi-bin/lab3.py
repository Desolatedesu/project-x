import os, sys
import cgi, cgitb
from math import *

cgitb.enable()
sys.stderr = sys.stdout

def lab(form):
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
