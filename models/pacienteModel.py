class Paciente:
    def __init__(self, nome, idade, CPF, email):
        self.nome = nome
        self.idade = idade
        self.CPF = CPF
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.CPF}, Email: {self.email}"