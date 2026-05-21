# componentes.py
from fasthtml.common import Div, H1, H2, P, Form, Input, Button, Ol, Li, A, Hr

def gerar_titulo(titulo, subtitulo): 
    return Div(
        H1(titulo),
        P(subtitulo),
        P('Esse componente foi gerado com FastHTML')
    )

def gerar_formulario():
    return Form(
        Input(type="text", name='tarefa', placeholder="Insira a tarefa a ser adicionada"), 
        Button("Enviar"), 
        method='post',
        action='/adicionar_tarefa',
        hx_post='/adicionar_tarefa',
        hx_target='#tarefas-lista',
        hx_swap='outerHTML'
    ) 

def gerar_lista_de_tarefas(lista_tarefas):
    # CORRIGIDO: Removido o 'hx style=' quebrado e unificado a string do estilo
    itens = [
        Li(
            f"{tarefa} ", 
            A("❌ Excluir", 
              href=f"/excluir_tarefa/{i}", 
              style="color: red; margin-left: 10px; text-decoration: none;")
        ) 
        for i, tarefa in enumerate(lista_tarefas)
    ]
    
    # Adicionamos id='tarefas-lista' para o HTMX saber exatamente onde atualizar na tela
    return Ol(*itens, id='tarefas-lista')