from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Libera o InfinityFree

@app.route('/')
def home():
    return "A IA está online! Use a rota /ia para conversar."

@app.route('/ia', methods=['POST'])
def processar_ia():
    dados = request.json
    pergunta = dados.get('pergunta', '')
    
    # Aqui depois entra sua lógica real da IA
    resposta_ia = f"Recebi sua pergunta: '{pergunta}'. (Isso é um teste do Python)"
    
    return jsonify({"resposta": resposta_ia})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
