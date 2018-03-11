#!/usr/bin/env python3.4

import os,sys
import time, datetime
import cgi, cgitb
import pymysql
import lab1, lab2, lab3

cgitb.enable()
sys.stderr  =  sys.stdout

print('''\
Content-type:text/html\r\n
''', end = '')

domen = "g03u36.nn2000.info"
words = ('http://',domen, '/cgi-bin/main.py')
href_py_file = "".join(words)

qr_string = cgi.FieldStorage()

function = qr_string.getvalue("function")
page_id = qr_string.getvalue("page_id")

if "function" not in qr_string:
	function = "page"

if "page_id" not in qr_string:
	page_id = 1
else:
	page_id = int(page_id)

#соединяемся с базой данных

try:
	db  =  pymysql.connect(host = "127.0.0.1", user = "g03u36", passwd = "mysql16", db = "g03u36", charset = "utf8", use_unicode = True) # Open database connection
except:
	print('Connection to database has failed!')
	sys.exit(0)


cur  =  db.cursor() # prepare a cur object using cursor() method

cur.execute("SELECT `page_title`, `page_keywords` FROM `sql_pages` WHERE `page_id` = {};".format( page_id ))
db_one  =  cur.fetchone()

page_title = str(db_one[0])
page_keywords = str(db_one[1])

print('''
<!doctype html>
<html lang="ru">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>{}</title>
	<meta name = "keywords" content = "{}">
	<link rel="shortcut icon" href="/img/1.png" type="image/png">
	<link rel="stylesheet" href="https://unpkg.com/normalize.css@8.0.0/normalize.css">
	<link rel="stylesheet" href="/css/index.css">
	<link href="https://fonts.googleapis.com/css?family=Fira+Sans+Extra+Condensed:400,400i,700,700i&amp;subset=cyrillic" rel="stylesheet">
</head>
<body>

'''.format(page_title, page_keywords), end = '')

print('''
<header>
<div class="wrapper">
	<div class="header__item header__logo">
	<a href="/cgi-bin/main.py">
		<img class="logo" src="/img/logo2.png" alt="Go to the main page">
	</a>
	</div>

	<ul class="header__item header__menu">
''')

cur.execute("SELECT `page_id`,`page_prior_navig`,`page_title` FROM `sql_pages` ORDER BY `sql_pages`.`page_prior_navig` DESC;")
db_all  =  cur.fetchall()

for result in db_all:

	if (int(result[0]) != 0):
		if (int(result[0]) == page_id):
			print ('''
				<li><a href = "{}?function=page&page_id={}" class = "active">
			'''.format( href_py_file, result[0] ), sep = '', end = '')
		else:
			print ('''
				<li><a href = "{}?function=page&page_id={}">
			'''.format( href_py_file, result[0] ), sep = '', end = '')

		print("{}</a></li>".format( result[2] ), end = '')

print('''
</ul>
</div>
</header>
''')

print ('''
<main>
<div class="wrapper body-wrapper">
''')

if (function == "page"):

	cur.execute("SELECT page_id FROM sql_pages;")
	pages = cur.fetchall()

	pageList = []

	for i in pages:
		pageList.append(i[0])

	if page_id == 2:
		lab1.lab(qr_string)
	elif page_id == 3:
		lab2.lab(qr_string)
	elif page_id == 4:
		lab3.lab(qr_string)
	else:
		for i in pageList:
			if (page_id == i):
				cur.execute("SELECT `page_content` FROM `sql_pages`  WHERE `page_id` = {};".format( page_id ))
				db_one = cur.fetchone()
				page_content = db_one[0]
				print(page_content, end = '')

print ('''
</div>
</main>
''')

with open('../public_html/footer.html', mode='r', encoding='utf-8') as file_read:
	for line in file_read:
		print(line)

print ('''
</body>
</html>
''')

db.close()
