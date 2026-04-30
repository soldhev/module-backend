from flask import Flask, render_template, request, redirect, url_for, flash
from database import inserir_cliente

app = Flask(__name__)

@app.route('/', methods=['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = {
        'nome': request.form.get('nome', '').strip(),
        'sobrenome': request.form.get('sobrenome', '').strip(),
        'endereco': request.form.get('endereco', '').strip(),
        'numero': request.form.get('numero', '').strip(),
        'complemento': request.form.get('complemento', '').strip(),
        'bairro': request.form.get('bairro', '').strip(),
        'cidade': request.form.get('cidade', '').strip(),
        'estado': request.form.get('estado', '').strip(),
        'data_nascimento': request.form.get('data_nascimento', '').strip(),
        'cpf': request.form.get('cpf', '').strip(),
        'rg': request.form.get('rg', '').strip(),
        'telefone': request.form.get('telefone', '').strip(),
        'email': request.form.get('email', '').strip(),
    }

    # Validação básica dos campos obrigatórios
    obrigatorios = ['nome', 'sobrenome', 'endereco', 'numero', 'bairro',
                    'cidade', 'estado', 'data_nascimento', 'cpf', 'telefone', 'email']
    
    for campo in obrigatorios:
        if not dados[campo]:
            flash(f'O campo "{campo.replace("_", " ").title()}" é obrigatório.', 'erro')
            return render_template('formulario.html', dados=dados)

    try:
        inserir_cliente(dados)
        return render_template('formulario.html', sucesso=True, nome=dados['nome'])
    except Exception as e:
        flash(f'Erro ao cadastrar cliente: {str(e)}', 'erro')
        return render_template('formulario.html', dados=dados)

@app.route('/listar')
def listar():
    from database import listar_clientes
    clientes = listar_clientes()
    return render_template('listar.html', clientes=clientes)

if __name__ == '__main__':
    from criar_banco import criar_banco
    criar_banco()
    app.run(debug=True)
