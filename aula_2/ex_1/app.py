#importar a classe do flask
from flask import Flask, render_template
#cria a aplicaçao flask
app = Flask (__name__)


@app.route("/")
def home():
    
    #varioveis python
    nome = "carlos"
    idade = "19"
    endereco = "venancio aires 93"
    bairro = "cb"

    #Envia as variaveis para o html
    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        endereco=endereco,
        bairro=bairro
    )
    
if __name__ == "__main__":
 app.run(debug=True)



