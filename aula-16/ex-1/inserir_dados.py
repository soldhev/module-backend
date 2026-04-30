import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# inserindo dados na tabela clientes

#executa  o comando sql para inserir o primeiro cliente
cursor.execute("""
INSERT INTO clientes(nome, telefone, email)
                VALUES(?, ?, ?)
                                
""",("Joao da silva", "519955113270", "joao@gmail.com"))

cursor.execute("""
INSERT INTO pets(nome, especie, idade, cliente_id)
                VALUES (?, ?, ?, ?)
                                
""",("mimi", "gato", 3, 2))

cursor.execute("""
INSERT INTO servicos(descricao, preco)
            VALUES (?, ?)
    
              
""",("consulta veterinaria", 80.00))
# salva todas as alteraçoes feitas no banco
conexao.commit()
#fecha a conexao com o banco de dados
conexao.close()
#exibe uma mensagem informando que o banco foi criado com sucesso
print("banco e tabelas criados com suceeso!")
