from flask import Flask # type: ignore
from flask import render_template

from flask import request

app = Flask(__name__)
@app.route("/")
def index ():
    #renderiza o arquivo index.html
    return render_template("index.html")

#processamento dos dados

#define a rota /dados (GET é padrao no flask)
@app.route("/dados")
def dados():
    # captura o valor enviando pelo campo "nome"
    nome = request.args.get("nome")
    # captura o valor enviado pelo campo "idade"
    idade = request.args.get("idade")
    
    #captura o valor enviado pelo campo "dataNascimento"
    
    dataNascimento = request.args.get("dataNascimento")
    
    
    # captura o valor enviado pelo campo "endereço"
    endereco = request.args.get("endereco")
    
    bairro = request.args.get("bairro")
    
    estado = request.args.get("estado")
    
    ceular = request.args.get("request")
    
    email = request.args.get("email")
    
    cpf = request.args.get("cpf")
    
    rg = request.args.get("rg")
    
    
    
    
    #verificar se os dados foram enviados
    if nome and idade and endereco and estado and dataNascimento and cpf and rg and email and ceular:
        mensagem = "Dados Cadastrados com Sucesso"
    else:
        mensagem = "Nenhum dado foi enviado"
    

    
    # enviar os dados para o template dados.html
    return render_template(
        "dados.html",
        idade=idade,
        dataNascimento=dataNascimento,
        endereco=endereco,
        bairro=bairro,
        estado=estado,
        ceular=ceular,
        email=email,
        cpf=cpf,
        rg=rg,
        mensagem=mensagem
    )

if __name__ == "__main__":
    app.run(debug = True)
     
    
