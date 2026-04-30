import sqlite3

conexao = sqlite3.connect("loja_carros.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT
        p.nome,
        p.cpf,
        c.modelo,
        c.marca,
        c.ano,
        c.preco,
        v.data_venda
    FROM vendas v
    JOIN pessoas p ON p.id = v.pessoa_id
    JOIN carros  c ON c.id = v.carro_id
""")

resultados = cursor.fetchall()

print(f"{'Nome':<15} | {'CPF':<13} | {'Modelo':<8} | {'Marca':<7} | {'Ano':<4} | {'Preço':>10} | Data")
print()

for linha in resultados:
    nome, cpf, modelo, marca, ano, preco, data = linha
    print(f"{nome:<15} | {cpf:<13} | {modelo:<8} | {marca:<7} | {ano:<4} | {preco:>10.2f} | {data}")

conexao.close()
