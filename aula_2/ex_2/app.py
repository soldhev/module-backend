#importa a classe flask para cirar a aplicaçao web
from flask import Flask, render_template
#cria a aplicaçao flask
app = Flask(__nome__)
#define a rota principal do site
@app.route("/")
def home ():
    s = "teste de impressão utilizando variaveis"
    n = 15
    d = 10.5
    t = "exemplo de txt 223123"
    b = True
    f = False

   #variaveis com formataçao 
decimal_normal = f"`{n:d}" #decimal simples
decimal_8 = f"{m:8d}" # 8 espaços
decimal_08 = f"{n:08d}" # 8 digitos com zero
decimal_float = f"{n:2f}" # 2 casas decimais


# mostranso o tipo da variavel e valor
tipos = {
"t": f"{t}" (tipo: {type(t).__name__})"
"n": f"{n}" (tipo: {type(n).__name__})"
"b": f"{b}" (tipo: {type(d).__name__})"
"d": f"{d}" (tipo: {type(b).__name__})"
"f": f"{f}" (tipo: {type(f).__name__})"

}
return ]render_template(
    s=s,
    n=n,
    d=d,
    t=t,
    b=b,
    f=f,
    decimal_normal=decimal_normal,
    decimal_8-decimal_8,
    decimal_08=decimal_08,
    decimal_float=decimal_float,
    
)

