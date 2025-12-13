from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso libera o InfinityFree para conversar com o Python

# Essa é a porta de entrada da sua IA
@app.route('/ia', methods=['POST'])
def processar_ia():
    # 1. Pega o que o usuário mandou no site
    dados = request.json
    pergunta_do_usuario = dados.get('pergunta', '')

    # --- AQUI VAI ENTRAR O SEU CÓDIGO DA IA DEPOIS ---
    # Por enquanto, vamos fazer um teste simples:
    resposta_ia = "O Python recebeu sua mensagem: " + pergunta_do_usuario
    # -------------------------------------------------

    # 2. Devolve a resposta para o site
    return jsonify({"resposta": resposta_ia})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
