from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

#Define a rota principal "/"
@app.route("/")
def index():
    return render_template("index.html")

#define a rota que recebe os dados via post
@app.route("/parouimpar", methods=["POST"])
def parouimpar():
    numero = int(request.form.get("numero"))
    #Criar uma lista vazia para armazenar os resultados
    resultados = []
    #loop que vai de 1 ate o numero informado no formulario
    for n in range(1, numero + 1):
        #verifica se o nunmero é par ou impar 
        if n % 2 == 0:
            #adiciona um dicionario com numero e tipo
            resultados.append({
                "numero":n,
                "tipo": "par",
                "cor": "red" 
            })
        else:
            resultados.append({
                "numero":n,
                "tipo":"impar",
                "cor": "yellow"
            })    
            #envia a lista de resultados para o template resultado.html
    return render_template("resultados.html", resultados=resultados)

if __name__=="__main__":
    app.run(debug=True)