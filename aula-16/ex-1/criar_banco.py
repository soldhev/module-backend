#importando a bibilioteca sqlite3 que ja vem instalado com o python 
import sqlite3

# cria ou conecta ao banco de dados chamado ...
conexao = sqlite3.connect("banco.db")

# cria um cursor para executar o comando    SQL 
cursor = conexao.cursor()

# executa o comando sql para criar a tabela clientes

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
               if integer primary key autoincrement,
               nome text not null,
               telefone text,
               email text
               );               
               """)
#executa o comando sql para criar a tabela pets
cursor.execute("""
CREATE TABLE IF NOT EXISTS pets(
               if integer primary key autoincrement,
               nome text not null,
               especie text not null,
               idade integer,
               cliente_id integer,
               FOREIGN KEY (cliente_id) REFERENCES cliente(id) 
               );              
                """)



#executa o comando sql para criar a tabela servicos
cursor.execute("""
CREATE TABLE IF NOT EXISTS servicos(
               id integer primary key autoincrement,
               descricao text not null,
               preco real not null
               );              
                """)


# salva todas as alteraçoes feitas no banco
conexao.commit()
#fecha a conexao com o banco de dados
conexao.close()
#exibe uma mensagem informando que o banco foi criado com sucesso
print("banco e tabelas criados com suceeso!")
