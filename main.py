''' Usaremos nessa aula o FastHtml para facilitar a escrita do código HTML. Ele é um micro framework para a construção de páginas web, que tem como objetivo facilitar a escrita de código HTML em Python. 
Ele é inspirado no Flask, mas tem uma sintaxe mais simples e intuitiva.
'''
# O "H-T-M-L" tem que ser todo maiúsculo aqui vvv
from fasthtml.common import FastHTML, serve

# E aqui também vvv
app = FastHTML()

@app.get('/')
def homepage():
    return '<h1>Bem-vindo ao site com FastHTML!</h1>'

if __name__ == "__main__":
   serve(port=5001) # Isso garante que ele use sempre essa porta 