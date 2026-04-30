from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
# define a rota para o cáuculo usando o match-case
@app.route("/cauculo_macth", methods=["POST"])
def cauculo_match():
    # captura os valores enviados via post
    nota1 = float(request.form.get("nota1"))
    nota2 = float(request.form.get("nota2"))
    nota3 = float(request.form.get("nota3"))
    nota4 = float(request.form.get("nota4"))
    
    resultado = None
   

#define a rota para caulcular usando if/else
@app.route("/cauculo_if",methods=["POST"])
def  cauculo_if():
    notas = float(request.form.get)("notas")
    num1 = float(request.form.get("num1"))
    num2 = float(request.form.get("num2"))
    operacao = request.form.get("operacao")
     
    
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2 
    elif operacao =="*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "erro: divisao por zero"
    else:
        resultado = "erro: operação invãlida"
        
        return render_template("resultado_if.html", resultado=resultado)
    
    if __name__ == "__main__":
        app.run(Debug=True)
    
             
    
