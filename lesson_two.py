from jinja2 import Template
from markupsafe import escape

# data = """
# {% raw %} Модуль Jinja вместо определения {{ name }} подставляет соответствующее значение {% endraw %}"""
# tm = Template(data)
# msg = tm.render(name='Muhammad')

# link = '''В HTML-документе ссылки определяются так:
# <a href="#">Ссылка</a>'''
#
# tm = Template("{{ link | e }}")
# msg = tm.render(link=link)
#
# with open('lesson_two2.html', 'w') as file:
#     file.writelines(msg)

# link = '''В HTML-документе ссылки определяются так:
# <a href="#">Ссылка</a>'''
#
# msg = escape(link)

cities = [
    {'id': 1, 'city': 'Moscow'},
    {'id': 5, 'city': 'Tver'},
    {'id': 7, 'city': 'Minsk'},
    {'id': 8, 'city': 'Smolenck'},
    {'id': 11, 'city': 'Kaluga'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == 'Moscow' -%}
    <option>{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
