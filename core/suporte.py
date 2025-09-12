from dataBase.crud.suporteCRUD import suporteCRUD
from models.suporteModel import Suporte

class Suporte:
    def __init__(self, nome: str, problema: str, email: str, nota: int = None):
        self.nome = nome
        self.problema = problema
        self.email = email
        self.nota = nota

    def registrar_suporte(self, conexao):
        suporte_crud = suporteCRUD(conexao)
        novo_suporte = Suporte(self.nome, self.problema, self.email, self.nota)
        suporte_crud.criarSuporte(novo_suporte)

    def exibir_suporte(self):
        print("----Menu de Suporte----")
        print("Como podemos ajudar?")
        print("(1) Falar com um atendente.")
        print("(2) Voltar ao menu principal.")

        escolha = int(input())

        if escolha == "1":
            Suporte.registrar_suporte()
    