import sqlite3

conexao = sqlite3.connect("loja_carros.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        nome  TEXT    NOT NULL,
        cpf   TEXT    NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS carros (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT    NOT NULL,
        marca  TEXT    NOT NULL,
        ano    INTEGER NOT NULL,
        preco  REAL    NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoa_id   INTEGER NOT NULL,
        carro_id    INTEGER NOT NULL,
        data_venda TEXT NOT NULL,
        FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
        FOREIGN KEY (carro_id)  REFERENCES carros(id)
    )
""")

conexao.commit()
conexao.close()

print("Banco de dados e tabelas criados com sucesso!")
