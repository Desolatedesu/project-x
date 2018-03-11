import os, sys
import cgi, cgitb

cgitb.enable()
sys.stderr = sys.stdout

def lab():
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
