class Paciente:
    def __init__(self, nome, idade, CPF, email, senha):
        self.nome = nome
        self.idade = idade
        self.CPF = CPF
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.CPF}, Email: {self.email}, Senha: {self.senha}"