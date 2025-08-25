class Paciente:
    def __init__(self, nome, idade, CPF):
        self.nome = nome
        self.idade = idade
        self.CPF = CPF

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.CPF}"