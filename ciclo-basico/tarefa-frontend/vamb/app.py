from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Isso serve para que o Vue acesse a API que estou criando

# Carregando os dados do CSV:
df = pd.read_csv("dados-flask-treino.csv")

# Criando a rota para listar os países disponíveis no csv:
@app.route("/paises")
def listar_paises():
    return jsonify(df["pais"].unique().tolist())

# Rota para recuperar os dados do país fornecido:
@app.route("/paises/<pais>")
def dados_pais(pais):
    dados = df[df["pais"] == pais].to_dict(orient="records")  # orient="records" faz com que cada linha do df vire um dicionário.
    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)
