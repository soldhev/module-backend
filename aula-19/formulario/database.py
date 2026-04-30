import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'clientes.db')

def get_conn():
    return sqlite3.connect(DB_PATH)

def inserir_cliente(dados):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nome, sobrenome, endereco, numero, complemento,
            bairro, cidade, estado, data_nascimento, cpf, rg, telefone, email)
        VALUES (:nome, :sobrenome, :endereco, :numero, :complemento,
            :bairro, :cidade, :estado, :data_nascimento, :cpf, :rg, :telefone, :email)
    ''', dados)
    conn.commit()
    conn.close()

def listar_clientes():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes ORDER BY id DESC')
    clientes = cursor.fetchall()
    conn.close()
    return clientes
