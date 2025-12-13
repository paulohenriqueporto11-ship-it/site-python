from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ==============================================================================
# DEPARTAMENTO 1: O CRIADOR (Gera códigos prontos)
# ==============================================================================
def departamento_criar(linguagem, alvo):
    # --- HTML ---
    if linguagem == "html":
        if "botao" in alvo or "button" in alvo:
            return "Aqui está um botão padrão:\n<button type='button'>Clique Aqui</button>"
        elif "input" in alvo or "campo" in alvo:
            return "Aqui está um campo de texto:\n<input type='text' placeholder='Digite algo...'>"
        elif "estrutura" in alvo or "basico" in alvo:
            return "<!DOCTYPE html>\n<html>\n<head>\n<title>Titulo</title>\n</head>\n<body>\n  <h1>Olá Mundo</h1>\n</body>\n</html>"
        elif "imagem" in alvo or "img" in alvo:
            return "<img src='caminho-da-foto.jpg' alt='Descricao da imagem' width='200'>"

    # --- PHP ---
    elif linguagem == "php":
        if "conexao" in alvo or "banco" in alvo:
            return "<?php\n$conn = new mysqli('localhost', 'user', 'pass', 'db');\nif ($conn->connect_error) die('Erro');\necho 'Conectado!';\n?>"
        elif "echo" in alvo or "texto" in alvo:
            return "<?php echo 'Olá, sou um script PHP!'; ?>"
        elif "if" in alvo:
            return "<?php\nif ($idade >= 18) {\n    echo 'Maior de idade';\n} else {\n    echo 'Menor de idade';\n}\n?>"

    # --- CSS ---
    elif linguagem == "css":
        if "fundo" in alvo or "cor" in alvo:
            return "body {\n  background-color: #f0f0f0;\n  color: #333;\n}"
        elif "centralizar" in alvo:
            return "div {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}"

    # --- JS ---
    elif linguagem == "js":
        if "alerta" in alvo or "popup" in alvo:
            return "alert('Isso é um alerta do JavaScript!');"
        elif "funcao" in alvo:
            return "function minhaFuncao() {\n  console.log('Executou!');\n}"

    return f"Entendi que você quer CRIAR algo em {linguagem}, mas não tenho o molde para '{alvo}' ainda."

# ==============================================================================
# DEPARTAMENTO 2: O PROFESSOR (Explica conceitos)
# ==============================================================================
def departamento_explicar(linguagem, alvo):
    base_conhecimento = {
        "html": {
            "div": "A <div> é uma caixa genérica usada para agrupar elementos e aplicar CSS.",
            "p": "A tag <p> serve para criar parágrafos de texto.",
            "form": "O <form> é usado para coletar dados do usuário e enviar para o servidor."
        },
        "php": {
            "variavel": "Em PHP, variáveis começam com $ (ex: $nome = 'João';).",
            "array": "Arrays guardam vários valores. Ex: $lista = ['a', 'b', 'c'];",
            "session": "Sessions servem para guardar dados do usuário enquanto ele navega (como login)."
        },
        "css": {
            "padding": "Padding é o espaço interno (entre o conteúdo e a borda).",
            "margin": "Margin é o espaço externo (fora da borda, afastando outros elementos)."
        },
        "js": {
            "let": "Let cria uma variável que pode mudar de valor depois.",
            "const": "Const cria uma variável que NÃO pode mudar (constante).",
            "console": "Console.log() serve para mostrar mensagens no painel de desenvolvedor (F12)."
        }
    }

    # Tenta buscar a explicação exata
    if linguagem in base_conhecimento:
        for chave, explicacao in base_conhecimento[linguagem].items():
            if chave in alvo:
                return f"EXPLICAÇÃO ({linguagem.upper()}): {explicacao}"
    
    return f"Sou especialista em {linguagem}, mas não sei explicar '{alvo}' ainda."

# ==============================================================================
# DEPARTAMENTO 3: O CORRETOR (Procura erros simples)
# ==============================================================================
def departamento_corrigir(linguagem, codigo_usuario):
    erros = []

    if linguagem == "php":
        if "$" not in codigo_usuario and ("=" in codigo_usuario):
            erros.append("Parece que você esqueceu o '$' antes da variável.")
        if ";" not in codigo_usuario and "echo" in codigo_usuario:
            erros.append("Faltou o ponto e vírgula (;) no final do comando echo.")

    elif linguagem == "html":
        if "<" in codigo_usuario and ">" not in codigo_usuario:
            erros.append("Você abriu uma tag '<' mas esqueceu de fechar com '>'.")
        if "src=" in codigo_usuario and ".jpg" not in codigo_usuario and ".png" not in codigo_usuario:
            erros.append("A tag de imagem parece estar sem a extensão do arquivo (.jpg, .png).")

    if len(erros) > 0:
        return "⚠️ Encontrei possíveis erros:\n" + "\n".join(erros)
    
    return "✅ Não encontrei erros óbvios de sintaxe (mas sou uma IA básica, teste o código!)."

# ==============================================================================
# CÉREBRO PRINCIPAL (Roteador)
# ==============================================================================
@app.route('/ia', methods=['POST'])
def processar_ia():
    dados = request.json
    texto = dados.get('pergunta', '').lower()
    
    # 1. IDENTIFICAR LINGUAGEM
    linguagem = "indefinido"
    if "php" in texto: linguagem = "php"
    elif "html" in texto: linguagem = "html"
    elif "css" in texto: linguagem = "css"
    elif "js" in texto or "javascript" in texto: linguagem = "js"

    # 2. IDENTIFICAR AÇÃO (CRIAR, EXPLICAR ou CORRIGIR)
    resposta = ""
    
    # Se o usuário pede para criar/fazer/gerar
    if any(x in texto for x in ["criar", "fazer", "gerar", "crie", "me da", "quero"]):
        if linguagem != "indefinido":
            resposta = departamento_criar(linguagem, texto)
        else:
            resposta = "Entendi que você quer criar algo, mas em qual linguagem? (HTML, PHP, JS...)"

    # Se o usuário pede explicação
    elif any(x in texto for x in ["oque", "o que", "explica", "como funciona", "significa"]):
        if linguagem != "indefinido":
            resposta = departamento_explicar(linguagem, texto)
        else:
            resposta = "Posso explicar, mas sobre qual linguagem? (Ex: 'O que é div em HTML?')"

    # Se o usuário pede correção ou manda código com erro
    elif any(x in texto for x in ["corrigir", "erro", "bug", "analisa", "ve se ta certo"]):
        if linguagem != "indefinido":
            resposta = departamento_corrigir(linguagem, texto)
        else:
            resposta = "Para corrigir, me diga qual é a linguagem do código."

    # Se não entendeu nada, tenta ser simpático
    else:
        resposta = "Ainda estou aprendendo! Tente: 'Criar botão HTML', 'Explicar variável PHP' ou 'Corrigir erro JS'."

    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
