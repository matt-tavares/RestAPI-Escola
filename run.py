from flask import Flask, jsonify, request
from business.businessTitulo import Titulo

app = Flask(__name__)

@app.route("/titulos", methods=["GET", "POST"])
def titulos():
    if request.method == "GET":
        titulos = Titulo.get_titulos()
        return jsonify(titulos)

    if request.method == "POST":
        dados = request.json['descricao']
        retorno = Titulo.post_titulo(dados)
        return retorno

@app.route("/titulo", methods=["GET", "PUT", "DELETE"])
def titulo():
    if request.method == "GET":
        try:
            id = int(request.json['id'])
            titulo = Titulo.get_titulo(id)
            return jsonify(titulo)
        except Exception as e:
            return str(e), 400

    if request.method == "PUT":
        try:
            id = int(request.json['id'])
            descricao = request.json['descricao']
            response = Titulo.put_titulo(descricao, id)
        except Exception as e:
            response = str(e), 400
        return response

    if request.method == "DELETE":
        try:
            id = request.json['id']
            response = Titulo.delete_titulo(id)
            return response
        except Exception as e:
            return str(e), 400


if __name__ == '__main__':
    app.run(debug=True)