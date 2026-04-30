import sqlite3

conexao = sqlite3.connect("loja_carros.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS vendas")

conexao.commit()
conexao.close()

print("Tabela vendas apagada com sucesso!")