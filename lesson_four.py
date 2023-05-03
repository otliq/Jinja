from jinja2 import Environment, FileSystemLoader, FunctionLoader

trades = [
    {'pair': 'CNYRUB', 'volume': 20000, 'pnl': 5000},
    {'pair': 'USDTRUB', 'volume': 2500, 'pnl': 15000},
    {'pair': 'TATN', 'volume': 450, 'pnl': 2500},
]


# file_loader = FileSystemLoader('templates')

def loadT(path):
    if path == 'index':
        return '''Symbol {{t.pair}}, Volume {{t.volume}}, P&L {{t.pnl}}'''
    else:
        return '''Data {{t}}'''


file_loader = FunctionLoader(loadT)
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(t=trades[0])

print(msg)
