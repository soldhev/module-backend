import sqlite3


class Conexao:
    @staticmethod
    def conectar():
        return sqlite3.connect("database.db")
    
    @staticmethod
    def criar_tabela():
        conn = Conexao.conectar()
        cursor = conn.cursor()
        cursor.execute("""
        create table if not exists usuario(
            id integer primary key autoincrement
            nome text,
            email text,
            senha text
            )               
        """)
        
        conn.commit()
        conn.close()