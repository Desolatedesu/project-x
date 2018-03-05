#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html\n')

with open('../public_html/header.html', mode='r') as file_read:
  for line in file_read:
    print(line)

filepath = ''
file_content = ''
list = []
form = cgi.FieldStorage()

if "file" in form:
  filepath = str(form["file"].value)

  try:
    file = open(filepath,'r', encoding="utf-8")

    file_content = file.read()

    print('<h2>File contents:</h2><p>{}</p>'.format(file_content))

    for word in file_content.split():
      if word[0].lower() in "eiuyo":
        list.append(word)
      else:
        continue

    print('<h2>Words with vowels:</h2><p>', list, '</p>');

    file.close()
  except FileNotFoundError:
    print('<div class="error">File doesn\'t exist</div>')
else:
  print('<div class="error">Enter a filename</div>')

with open('../public_html/lab1.html', mode='r') as file_read:
  for line in file_read:
    print(line)

with open('../public_html/footer.html', mode='r') as file_read:
  for line in file_read:
    print(line)
