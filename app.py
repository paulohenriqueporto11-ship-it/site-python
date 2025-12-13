from flask import Flask, request, jsonify
from flask_cors import CORS
from fuzzywuzzy import process

app = Flask(__name__)
CORS(app)

# --- CÉREBRO DA IA (Base de Conhecimento) ---
# Aqui é onde você "treina" ela. Quanto mais coisas você colocar, mais inteligente ela fica.
cerebro = {
    "variavel": "Uma variável é como uma caixa onde você guarda dados. Em Python: nome = 'valor'",
    "função": "Função é um bloco de código que faz uma tarefa específica. Ex: def minha_funcao():",
    "loop": "Loop (ou laço) serve para repetir comandos. O 'for' e o 'while' são os mais usados.",
    "if": "O 'if' serve para tomar decisões. Se algo for verdade, ele executa o código.",
    "python": "Python é uma linguagem de alto nível, focada em legibilidade e muito usada em IA.",
    "html": "HTML não é programação, é marcação. Ele cria a estrutura do site.",
    "css": "CSS serve para dar estilo e cor para o HTML.",
    "array": "Array (ou Lista em Python) é uma variável que guarda vários valores de uma vez.",
    "api": "API é uma forma de dois sistemas conversarem entre si.",
    "bug": "Bug é um erro no código que faz ele rodar de jeito inesperado.",
    "hello world": "Hello World é o primeiro programa que fazemos para testar uma linguagem."
}

@app.route('/')
def home():
    return "IA Própria (Baseada em Regras) Online!"

@app.route('/ia', methods=['POST'])
def processar_ia():
    dados = request.json
    pergunta_usuario = dados.get('pergunta', '').lower() # Transforma em minusculo

    # Lógica de Inteligência (Busca por similaridade)
    # A IA tenta encontrar a chave no dicionário que mais parece com a pergunta do usuário
    melhor_match, pontuacao = process.extractOne(pergunta_usuario, cerebro.keys())

    # Se a certeza for maior que 50%, ela responde
    if pontuacao > 50:
        resposta_ia = cerebro[melhor_match]
        confianca = f"(Certeza: {pontuacao}%)"
    else:
        resposta_ia = "Ainda não sei sobre isso. Me ensine programando novas linhas no 'cerebro'!"
        confianca = "(Não entendi)"

    return jsonify({
        "resposta": resposta_ia,
        "debug": confianca
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
