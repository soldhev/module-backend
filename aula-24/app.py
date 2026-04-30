from flask import Flask, render_template, request, redirect, url_for
from controllers.usuario_controller import UsuarioController
from database.conexao import Conexao

app = Flask(__name__)
Conexao.criar_tabela()

@app.route("/")
def login():
    return render_templete("login.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    
    controller = UsuarioController()
    controller.cadastrar(nome, email, senha)
    
    return """
    <script>
    alert("usuario cadastrado com sucesso !")
    window.location.href="/";
    </script>
    """
    
@app.route("/logar", methods=["POST"])
def logar():
    email = request.form.get("email")
    senha = request.form.get("senha")
    
    controller = UsuarioController()
    #verifica login
    if controller.login(email, senha):
        return"""
    <script>
    alert("E-mail ou senha invalidos");
    window.location.href="/";
    </script>
    """
    if __name__ == "__main__":
        app.run(debug=True)
