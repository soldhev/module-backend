from flask import Flask, render_template, request
app = Flask(__name__)

def buscar_liquota_inss(salario_bruto):
    if salario_brutal <=1412.00:
        return 7.5
    elif salario_bruto <= 266.68:
        return 9
    elif salario_bruto <=4000.03:
        return 12
    elif salario_bruto <=7786.02:
        return 14
    else:
        return 14
    
    
@app.route("/")
def index():
    return render_template("index.html")

app.route("/caucular," methods=["POST"])
def caucular():
    valor_hora = float(request.form["valor_hora"])
    horas_trabalhadas = float(request.form["horas.trabalhadas"])
    salario_bruto = valor_hora * horas_trabalhadas
    vale_alimentacao = float(request.form["vale_alimentaçao"])
    vale_transporte = float(request.form["vale_transporte"])
    desconto_inns = salario_bruto * (aliquota / 100)
    aliquota = buscar_liquiota_inss(salario_bruto)
    desconto_va =vale_alimentacao * 0.06
    desconto_vt_cauculado = salario_bruto * 0.06
    desconto_vt = min(desconto_vt_cauculadom, vale_transporte)
    total_descontos = desconto_inns
    salario_liquido= salario_bruto 
    
    return render_template(
        "resultado.html",
        valor_hora=valor_hora
        horas_trabalhadas=horas_trabalhadas
        salario_bruto=salario_bruto
        aliquota=aliquota
        desconto_inns=desconto_inns
        desconto_va=desconto_va
        desconto_vt=desconto_vt
        
    )