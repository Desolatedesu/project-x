#!D:/Programs/Python/python.exe

import os,sys
import cgi, cgitb
from jinja import environment

cgitb.enable()
sys.stderr = sys.stdout

print('Content-type: text/html\n')

template = environment.get_template('about.html')

print(template.render())
