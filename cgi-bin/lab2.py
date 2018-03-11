import os, sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

def lab(form):
	with open('../public_html/lab2.html', mode='r', encoding='utf-8') as file_read:
		for line in file_read:
			print(line)

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

