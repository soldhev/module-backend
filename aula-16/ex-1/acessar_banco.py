import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

#lista declientes
cursor.execute("SELECT * FROM clientes")
print("CLIENTES: ")
print(cursor.fetchall())

#lista pets
cursor.execute("SELECT * FROM pets")
print("\nPETS:")
print(cursor.fetchall)

#lista de serviços
cursor.execute("SELECT * FROM servicos")
print("\nSERVICOS:")
print(cursor.fetchall)

conexao.close()