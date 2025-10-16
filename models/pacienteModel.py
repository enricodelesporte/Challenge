class Paciente:
    def __init__(self, id, nome, idade, CPF, email, senha, CEP):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.CPF = CPF
        self.email = email
        self.senha = senha
        self.CEP = CEP

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.CPF}, Email: {self.email}, Senha: {self.senha}, CEP: {self.CEP}"