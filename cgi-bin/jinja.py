from jinja2 import Environment, FileSystemLoader, select_autoescape

environment = Environment(
  loader=FileSystemLoader('../src/views'),
  autoescape=select_autoescape(['html', 'xml'])
)
