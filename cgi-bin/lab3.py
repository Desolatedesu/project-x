import os, sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

def lab(form):
	with open('../public_html/lab3.html', mode='r', encoding='utf-8') as file_read:
		for line in file_read:
			print(line)

	n = 0
	list = []

	if "x" in form and "y" in form and "z" in form:
		list.append(str(form["x"].value))
		list.append(str(form["y"].value))
		list.append(str(form["z"].value))

		print("<h2>Results</h2>")

		for i, word in enumerate(list, start = 1):
			for letter in word:
				if letter.lower() in "aeouiyауеоюёяиэы":
					n = n + 1
			print("<p>Строка ", str(i), ": ", str(n), " гласных букв</p>")
			n = 0
	else:
		print('<div class="error">Введите данные</div>')

