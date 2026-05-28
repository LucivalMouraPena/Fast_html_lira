from fasthtml.common import *
import random
import json

app, rt = fast_app()

# -------------------------
# Banco de perguntas
# -------------------------
todas_perguntas = [

    {
        "pergunta": "Qual comando define uma função em Python?",
        "alternativas": ["function", "def", "func", "create"],
        "correta": 1
    },

    {
        "pergunta": "Como iniciar um loop for?",
        "alternativas": ["for x in y", "loop x", "foreach", "repeat"],
        "correta": 0
    },

    {
        "pergunta": "Qual palavra retorna valores?",
        "alternativas": ["send", "return", "back", "output"],
        "correta": 1
    },

    {
        "pergunta": "Qual símbolo cria lista?",
        "alternativas": ["()", "[]", "{}", "//"],
        "correta": 1
    },

    {
        "pergunta": "Qual comando imprime texto?",
        "alternativas": ["echo()", "show()", "print()", "write()"],
        "correta": 2
    },

    {
        "pergunta": "Qual operador compara igualdade?",
        "alternativas": ["=", "==", "!=", ">="],
        "correta": 1
    },

    {
        "pergunta": "Qual estrutura toma decisões?",
        "alternativas": ["loop", "if", "class", "import"],
        "correta": 1
    },

    {
        "pergunta": "Como comentar uma linha?",
        "alternativas": ["//", "#", "--", "/*"],
        "correta": 1
    },

    {
        "pergunta": "Qual tipo armazena verdadeiro/falso?",
        "alternativas": ["string", "int", "bool", "float"],
        "correta": 2
    },

    {
        "pergunta": "Qual palavra importa bibliotecas?",
        "alternativas": ["using", "require", "include", "import"],
        "correta": 3
    },

    {
        "pergunta": "Qual função converte para inteiro?",
        "alternativas": ["str()", "float()", "int()", "bool()"],
        "correta": 2
    },

    {
        "pergunta": "Qual comando encerra loop?",
        "alternativas": ["stop", "exit", "break", "finish"],
        "correta": 2
    },

    {
        "pergunta": "Qual comando continua loop?",
        "alternativas": ["continue", "next", "skip", "pass"],
        "correta": 0
    },

    {
        "pergunta": "Qual símbolo cria dicionário?",
        "alternativas": ["[]", "()", "{}", "<>"],
        "correta": 2
    },

    {
        "pergunta": "Qual função mede tamanho?",
        "alternativas": ["size()", "count()", "len()", "measure()"],
        "correta": 2
    },

    {
        "pergunta": "Qual comando remove item de lista?",
        "alternativas": ["delete()", "remove()", "pop()", "erase()"],
        "correta": 2
    },

    {
        "pergunta": "Qual palavra cria classe?",
        "alternativas": ["object", "class", "new", "struct"],
        "correta": 1
    },

    {
        "pergunta": "Qual biblioteca trabalha com datas?",
        "alternativas": ["date", "clock", "datetime", "timeplus"],
        "correta": 2
    },

    {
        "pergunta": "Qual comando abre arquivos?",
        "alternativas": ["file()", "open()", "read()", "load()"],
        "correta": 1
    },

    {
        "pergunta": "Qual comando trata erros?",
        "alternativas": ["catch", "error", "try", "safe"],
        "correta": 2
    }

]

# -------------------------
# Controle de perguntas usadas
# -------------------------
perguntas_usadas = []

# -------------------------
# Página principal
# -------------------------
@rt("/")
def homepage():

    global perguntas_usadas

    disponiveis = [
        p for p in todas_perguntas
        if p not in perguntas_usadas
    ]

    # Reinicia quando acabar perguntas
    if len(disponiveis) < 5:
        perguntas_usadas.clear()
        disponiveis = todas_perguntas.copy()

    perguntas_sorteadas = random.sample(disponiveis, 5)

    perguntas_usadas.extend(perguntas_sorteadas)

    quiz_json = json.dumps(perguntas_sorteadas)

    return Div(

        Style("""

        body{
            background:#0f172a;
            color:white;
            font-family:Arial;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            margin:0;
        }

        .container{
            width:750px;
            background:#1e293b;
            padding:40px;
            border-radius:20px;
            box-shadow:0 0 30px rgba(0,0,0,0.5);
        }

        h1{
            text-align:center;
            margin-bottom:30px;
        }

        .pergunta{
            font-size:24px;
            margin-bottom:25px;
            animation:fade 0.5s;
        }

        .alternativa{
            background:#334155;
            padding:15px;
            border-radius:12px;
            margin-bottom:15px;
            cursor:pointer;
            transition:0.3s;
            border:2px solid transparent;
        }

        .alternativa:hover{
            transform:scale(1.03);
            background:#475569;
            border-color:#3b82f6;
        }

        .selecionada{
            border:2px solid #3b82f6;
        }

        .correta{
            background:#16a34a !important;
        }

        .errada{
            background:#dc2626 !important;
        }

        button{
            background:#3b82f6;
            color:white;
            border:none;
            padding:14px 20px;
            border-radius:10px;
            cursor:pointer;
            margin-top:20px;
            font-size:16px;
            transition:0.3s;
        }

        button:hover{
            background:#2563eb;
            transform:scale(1.03);
        }

        .fundo-barra{
            background:#334155;
            border-radius:20px;
            overflow:hidden;
            margin-bottom:30px;
            height:12px;
        }

        .barra{
            height:100%;
            width:0%;
            background:#3b82f6;
            transition:0.5s;
        }

        @keyframes fade{
            from{
                opacity:0;
                transform:translateY(10px);
            }

            to{
                opacity:1;
                transform:translateY(0);
            }
        }

        """),

        Div(

            H1("Quiz Python IA"),

            Div(
                Div(cls="barra", id="barra"),
                cls="fundo-barra"
            ),

            Div(id="quiz"),

            cls="container"
        ),

        Script(f"""

        const quiz = {quiz_json};

        let atual = 0;
        let pontos = 0;
        let selecionada = null;

        function carregarPergunta() {{

            let q = quiz[atual];

            let html = `
                <div class="pergunta">
                    Pergunta ${{atual + 1}} de ${{quiz.length}}
                    <br><br>
                    ${{q.pergunta}}
                </div>
            `;

            q.alternativas.forEach((alt, index) => {{

                html += `
                    <div class="alternativa"
                        onclick="selecionar(${{index}}, this)">

                        ${{String.fromCharCode(65 + index)}}) ${{alt}}

                    </div>
                `;
            }});

            html += `
                <button onclick="proximaPergunta()">
                    Próxima Pergunta
                </button>
            `;

            document.getElementById("quiz").innerHTML = html;

            atualizarBarra();
        }}

        function selecionar(index, elemento) {{

            if(selecionada !== null){{
                return;
            }}

            selecionada = index;

            let correta = quiz[atual].correta;

            let alternativas =
                document.querySelectorAll(".alternativa");

            if(index === correta){{

                elemento.classList.add("correta");

                pontos++;
            }}
            else{{

                elemento.classList.add("errada");

                alternativas[correta]
                    .classList.add("correta");
            }}
        }}

        function proximaPergunta() {{

            if(selecionada === null) {{
                alert("Selecione uma alternativa.");
                return;
            }}

            setTimeout(() => {{

                atual++;
                selecionada = null;

                if(atual < quiz.length) {{
                    carregarPergunta();
                }}
                else {{
                    resultadoFinal();
                }}

            }}, 500);
        }}

        function atualizarBarra() {{

            let progresso =
                ((atual + 1) / quiz.length) * 100;

            document.getElementById("barra")
                .style.width = progresso + "%";
        }}

        function resultadoFinal() {{

            let nivel = "";

            if(pontos <= 2) {{
                nivel = "Nível 1 - Iniciante";
            }}
            else if(pontos <= 4) {{
                nivel = "Nível 2 - Intermediário";
            }}
            else {{
                nivel = "Nível 3 - Avançado";
            }}

            document.getElementById("barra")
                .style.width = "100%";

            document.getElementById("quiz").innerHTML = `

                <h2>Quiz Finalizado</h2>

                <p>
                    Você acertou
                    <strong>${{pontos}}</strong>
                    de
                    <strong>${{quiz.length}}</strong>
                    perguntas.
                </p>

                <h3>${{nivel}}</h3>

                <button onclick="location.reload()">
                    Jogar Novamente
                </button>
            `;
        }}

        carregarPergunta();

        """)
    )


# -------------------------
serve(reload=False)
# -------------------------
if __name__ == "__main__":
    serve(reload=False)