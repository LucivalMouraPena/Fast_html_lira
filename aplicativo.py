from fasthtml.common import *
from componentes import gerar_titulo, gerar_formulario, gerar_lista_de_tarefas
from starlette.responses import RedirectResponse

# -------------------------
# Banco de dados temporário (memória)
# -------------------------
tarefas_salvas = [
    "Fazer o café",
    "Estudar FastHTML",
    "Dar um grau no código"
]

app, rt = fast_app()


# -------------------------
# Página principal
# -------------------------
@rt("/")
def homepage():
    return Div(
        gerar_titulo("Central de Tarefas do Usuario", "Projeto versionado com GitHub"),
        Hr(),

        H2("Minhas Tarefas Atuais:"),
        gerar_lista_de_tarefas(tarefas_salvas),

        Hr(),

        H2("Adicionar Nova Tarefa:"),
        gerar_formulario()
    )


# -------------------------
# Adicionar tarefa
# -------------------------
@rt("/adicionar_tarefa", methods=["post"])
def post_tarefa(tarefa: str):
    print(f"✅ Nova tarefa recebida: {tarefa}")

    if tarefa and tarefa.strip():
        tarefas_salvas.append(tarefa.strip())

    return gerar_lista_de_tarefas(tarefas_salvas)


# -------------------------
# Excluir tarefa
# -------------------------
@rt("/excluir_tarefa/{id}")
def excluir_tarefa(id: int):
    if 0 <= id < len(tarefas_salvas):
        tarefa_removida = tarefas_salvas.pop(id)
        print(f"🗑️ Tarefa excluída: {tarefa_removida}")

    return RedirectResponse(url="/", status_code=303)


# -------------------------
# Rodar servidor
# -------------------------
if __name__ == "__main__":
    serve()