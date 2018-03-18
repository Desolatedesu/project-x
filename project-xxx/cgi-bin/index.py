#!/usr/bin/env python3.4

import os, sys
import cgi, cgitb
import pymysql
import lab1, lab2, lab3

cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type:text/html\r\n
''', end = '')

form = cgi.FieldStorage()

id = form.getvalue("id")

if "id" not in form:
	id = 0
else:
	id = int(id)

# db

try:
	db = pymysql.connect(host = "127.0.0.1", user = "g03u40", passwd = "mysql16", db = "g03u40", charset = "utf8", use_unicode = True)
except:
	print('Не удалось соединиться с базой данных')
	sys.exit(0)

cur = db.cursor()

cur.execute("SELECT `title`, `keywords`, `content` FROM `pages` WHERE `id` = {};".format(id))
item = cur.fetchone()

title = str(item[0])
keywords = str(item[1])
content = str(item[2])

print('''
<!doctype html>
<html lang="ru">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>{}</title>
	<meta name="keywords" content="{}">
	<link rel="stylesheet" href="/css/index.css">
</head>
<body>
'''.format(title, keywords), end = '')

print('''
<header>
	<a class="main" href="/cgi-bin/index.py">На главную</a>
</header>
<main>
	<h1>{}</h1>
	<p>{}</p>
'''.format(title, content), end = '')

if id == 0:
	print('<ul>')

	cur.execute("SELECT `id`, `title` FROM `pages`")
	items = cur.fetchall()

	for result in items:
		print('''
			<li><a href="/cgi-bin/index.py?id={}">{}</a></li>
		'''.format(result[0], result[1]), sep = '', end = '')

	print('</ul>')

cur.execute("SELECT id FROM pages;")
pages = cur.fetchall()

pageList = []

for i in pages:
	pageList.append(i[0])

if id == 1:
	lab1.lab(form)
elif id == 2:
	lab2.lab()
elif id == 3:
	lab3.lab(form)

print('''
</div>
</main>
</body>
</html>
''')

db.close()
