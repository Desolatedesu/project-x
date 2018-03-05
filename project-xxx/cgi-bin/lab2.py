#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html;charset=windows-1251\n')

with open('../public_html/header.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

with open('../public_html/lab2.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)

array = [2, 3, 5, -7, 11, -13]
i = 0
print("<p>Начальный массив:</p><p>")

while i < len(array):
	print(array[i])
	i = i + 1

i = 0

while i < len(array):
	if array[i] < 0:
		array.insert(i + 1, array[i]**2)
	i = i + 1

i = 0

print("</p><p>Конечный массив</p><p>")

while i < len(array):
	print(array[i])
	i = i + 1

print("</p>")

with open('../public_html/footer.html', mode='r', encoding='utf-8') as file_read:
  for line in file_read:
    print(line)
