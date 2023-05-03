from jinja2 import Environment, FileSystemLoader, FunctionLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='t.me/otliq', title='Trader')

with open('lesson_five.html','w') as file:
    file.writelines(msg)
print(msg)
