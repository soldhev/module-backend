class Pessoa:
    def __init__(self, nome, idade , cpf, email, telefone, estado, cidade, endereco):
        self.nome = nome
        self.idade = idade 
        self.telefone = telefone
        self.cpf = cpf = cpf
        self.estado = estado 
        self.email = email
        self.cidade = cidade
        self.endereco = endereco
    
    def dados_formatados(self):
        return{
            "Nome": self.nome,
            "Idade": self.idade,
            "Cpf": self.cpf,
            "Cidade": self.cidade,
            "Estado": self.estado,
            "Telefone": self.telefone,
            "Endereco": self.endereco,
            "Email": self.email
        }    