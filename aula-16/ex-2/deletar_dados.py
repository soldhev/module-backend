import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
# deletye na tabela peys
#deleta o pet com o id = 2
#é importante deletar primeiro o pet, por cause da chave estrangeira
cursor.execute(""" 
DELETE FROM clientes
                where id = 2
                               
""",(2,))
conexao.commit()
conexao.close()
print("dados deletados com sucesso!")