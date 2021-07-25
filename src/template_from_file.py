from mako.template import Template
from mako import exceptions

try:
  mytemplate = Template(filename='configs/templates/basic.tmpl', module_directory='/tmp/mako_modules')
  print(mytemplate.render(name='jack'))
except:
  print(exceptions.text_error_template().render())

anotherTemplate = Template(filename='configs/templates/formula.tmpl')
print(anotherTemplate.render())


anotherTemplate2 = Template(filename='configs/templates/html_example.tmpl')
print(anotherTemplate2.render(names=['syu', 'pudding', 'pu'], data={'key_some': 'myValue.com'}))