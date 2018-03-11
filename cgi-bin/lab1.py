#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

def lab(form):

	with open('../public_html/lab1.html', mode='r', encoding='utf-8') as file_read:
		for line in file_read:
			print(line)

	filepath = ''
	file_content = ''
	list = []

	if "file" in form:
		filepath = str(form["file"].value)

		try:
			file = open(filepath,'r', encoding="utf-8")

			file_content = file.read()

			print('<h2>File contents:</h2><p>{}</p>'.format(file_content))

			for word in file_content.split():
				if word[0].lower() in "eiuyoaаоуюиыэеёя":
					list.append(word)
				else:
					continue

			print('<h2>Words with vowels:</h2><p>', list, '</p>');

			file.close()
		except FileNotFoundError:
			print('<div class="error">File doesn\'t exist</div>')
	else:
		print('<div class="error">Enter a filename</div>')
