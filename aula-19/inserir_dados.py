import sqlite3

conexao = sqlite3.connect("loja_carros.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    INSERT INTO pessoas (nome, cpf) VALUES
    ('João Pereira', '11111111111'),
    ('Maria Costa',  '22222222222')
""")
 
cursor.execute("""
    INSERT INTO carros (modelo, marca, ano, preco) VALUES
    ('Corolla', 'Toyota', 2022, 120000.00),
    ('Civic',   'Honda',  2021, 115000.00)
""")

cursor.execute("""
    INSERT INTO vendas (pessoa_id, carro_id, data_venda) VALUES
    (1, 1, '2024-01-10'),
    (2, 2, '2024-01-11')
""")

conexao.commit()
conexao.close()

print("Dados inseridos com sucesso!")
