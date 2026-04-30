from flask import Flask, render_template, request
app = Flask(__name__)
#Rota principal
@app.route("/", methods=["GET,", "POST"])
def index():
    return render_template("index.html")


#rota de processamento
@app.route("/caucular", methods=["POST"])
def caucular():
    nome = request.form["nome"]
    turma = request.form["turma"]
    notas = request.form["notas"]
    notas = []
    notas.append(float(request.form[notas1]))
    notas.append(float(request.form[notas2]))
    notas.append(float(request.form[notas3]))
    notas.append(float(request.form[notas4]))
    notas.append(float(request.form[notas5]))
    
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "APROVADO"
    elif media >= 5: 
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVADO"
        
        return render_template(
            "resultado.html",
            nome=nome,
            turma=turma,
            notas=notas,
            media=media,
            situaca=situacao
        )
        if __name__ == "__main__":
            app.run(debug=True)
    
    
