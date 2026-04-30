import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'clientes.db')

def criar_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            nome            TEXT NOT NULL,
            sobrenome       TEXT NOT NULL,
            endereco        TEXT NOT NULL,
            numero          TEXT NOT NULL,
            complemento     TEXT,
            bairro          TEXT NOT NULL,
            cidade          TEXT NOT NULL,
            estado          TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            cpf             TEXT NOT NULL,
            rg              TEXT,
            telefone        TEXT NOT NULL,
            email           TEXT NOT NULL,
            criado_em       DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso.")

if __name__ == '__main__':
    criar_banco()
