from database.conexao import Conexao

from models.usuario import Usuario

from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioController:
     def casdastrar(self, nome, email, senha):
         
         #criptografar a senha
         senha_hash = generate_password_hash(senha)
         #cria objeto usuario 
         usuario = usuario(nome, email, senha_hash)
         
         conn = Conexao.conectar()
         cursor = conn.cursor()
         cursor.execute("""
         insert into usuario(nome, email, senha)
                    values(?,?,?)                
         """,(usuario.get_nome(), usuario.get_email(), usuario.get_senha()) 
         )
         conn.commit()
         conn.close()
         def login(self, email, senha);
         conn = Conexao.conectar()
         cursor = conn.cursor()
         
         #busca usuario no banco 
         cursor.execute("SELECT senha FROM usuario Where email = ?", (email,))
         resultado = cursor.fetchone()
         conn.close()
         
         #se encontrar o usuario
         if resultado:
             senha_hash = resultado[0]
             # verifica a senha 
             return check_password_hash(senha_hash, senha)
         #se nao encontar 
         return False