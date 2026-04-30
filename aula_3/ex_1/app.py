from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    #Trabalhando com funçoes
    # define uma funçao que retorna uma mensagem
    def msg():
        return "hello world"
        mensagem = msg()

    # funçao que recebe um nome
    def nomeAluno(aluno):
        return aluno
    
    #Lista de alunos(chamada pela funçao)
    aluno = [
        nomeAluno("Carlos"),
        nomeAluno("Sarah"),
        nomeAluno("solrac"),
        nomeAluno("Sizzy")
    ]
# funçao que recebe dois argumentos, nome e idade
def nomeIdade(nome, idade):
    return f"Seu nome é: {nome}, e sua idade é {idade}"
#lista com o nome e idade
pessoas  = [
    nomeIdade("Juvenildo", 20),
    nomeIdade("manuela", 19),
    nomeIdade("Vladimir", 56),
    nomeIdade("Maria", 43)
]
#declaração de variavel do tipo global
global b
#Funçao para somar
def soma (a):
    global b
    b = a + 5

    #chama a funçao

    soma(10)



    valor b = b

    #outro exemplo de variavel global
    global a
    a = 1
    a = 2 

def caucula():
    global a,b
    b = a + b

caucula()
resultado_cauculo  = b

# envia todos os dados para o html
return render_template(
    "index.html",
    mensagem=mensagem,
    alunos=alunos,
    pessoa=pessoas,
    valor_b=valor_b,
    resultado_cauculo=resultado_cauculo
)



   