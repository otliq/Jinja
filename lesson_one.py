from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


per = Person('Muhammad', 20)

tm = Template("Assalamu aleykum, my name is {{ p.name }} and I'am {{ p.age }} years old")
msg = tm.render(p=per)

print(msg)
