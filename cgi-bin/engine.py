#!/usr/bin/env python3.4

import os, sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type: text/html\r\n
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title>Desu Page</title>
		<link rel="shortcut icon" href="/3.png" type="image/png">
		<link rel="stylesheet" href="https://unpkg.com/normalize.css@8.0.0/normalize.css">
		<link rel="stylesheet" href="./css/index.css">
		<link href="https://fonts.googleapis.com/css?family=Fira+Sans+Extra+Condensed:400,400i,700,700i&amp;subset=cyrillic" rel="stylesheet">
	</head>
	<body>
	''')

with open('../public_html/header.html', mode='r', encoding='utf-8', errors=None) as file_read:
	for line in file_read:
		print(line)

print('''
	<div class='wrapper body-wrapper'>
	''')

with open('../public/main.html', mode='r', encoding='utf-8', errors=None) as file_read:
	for line in file_read:
		print(line)

print('''
	</div>
	''')

with open('../public/footer.html', mode='r', encoding='utf-8', errors=None) as file_read:
	for line in file_read:
		print(line)

print('''
</div>
</body>
</html>
''')
