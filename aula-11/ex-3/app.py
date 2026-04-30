from flask import Flask, render_template, request
from pessoa import Pessoa

app = Flask(__name__)
    
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Rota de processamento
@app.route("/resultado", methods=["POST"])
def resultado():
    # Recebe os dados enviados pelo formulário
    nome = request.form["nome"]
    idade = request.form["idade"]
    endereco = request.form["endereco"]
    cidade = request.form["cidade"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    estado = request.form["estado"]
    
    pessoa = Pessoa(nome, idade, cpf, email, estado, cidade, telefone)
    
    return render_template(
        "resultado.html",
        da
    )

if __name__ == "__main__":
    app.run(debug=True)