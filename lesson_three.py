# Filters and Macros macro,call

from jinja2 import Template

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Volvo', 'price': 44300},
#     {'model': 'Volkswagen', 'price': 21300}
# ]
#
# tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
# tpl1 = "Самый дорогой автомобиль {{ (cs | max(attribute='price')).model }}"
# tpl2 = "Самый бюджетный автомобиль {{ (cs | min(attribute='price')).model }}"
# tpl3 = "Автомобиль {{ cs | replace('o','O') }}"
#
# tm = Template(tpl3)
# msg = tm.render(cs=cars)
# print(msg)

persons = [
    {'name': 'MuhammadAli', 'old': 26, 'weight': 78.5},
    {'name': 'MuhammadKodir', 'old': 22, 'weight': 72},
    {'name': 'MuhammadZoir', 'old': 20, 'weight': 65},
]
#
# tpl = '''
# {%- for u in users -%}
# {% filter upper %}{{u.name}}{% endfilter %}
# {% endfor -%}
# '''
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)

# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''

html = '''
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)
