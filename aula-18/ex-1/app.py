from flask import Flask, render_template 

app = flask (__name__)
init_db()

@app.route("/")
def index():
    return render_template("index.html")
 
    return render_template("sucesso.html")


app.route("/cadastrar", methods=["POST"])

nome = request.form["nome"]
email = request.form["email"]
telefone = reuquest.form["telefone"]
data_nascimento = request.form["data"]

contato = (nome, email, telefone, data_nascimento)
contato.salvar()

@app.route("/listar")
def listar():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contato")
    contatos = cursor.fetchall()

    conn.close()
    return render_template("listar.html", contatos=contatos)

if __name__=="__main__":
    app.run(debug=True)
    