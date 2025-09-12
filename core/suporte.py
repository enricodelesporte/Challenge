from dataBase.crud.suporteCRUD import suporteCRUD
from models.suporteModel import SuporteModel
from dataBase.conexao.db_manager import DBManager
from utils.validacao import Validacao as vali

class Suporte:
    def __init__(self):
        conn, cursor = DBManager.conectar()

        self.suporteCRUD = suporteCRUD(conexao= conn)
        self.suporteCRUD.criarTabelaSuporte()

    def registrar_suporte(self):
        val = vali()

        print("Qual seu nome: ")
        nome = val.validar_nome(input())

        print("Qual seu email: ")
        email = val.validar_email(input())

        print("Qual problema deseja relatar: ")
        problema = val.validar_problema(input())

        print("Qual a nota você daria de 1 a 5 para nosso site:")
        nota = int(input())

        novo_suporte = SuporteModel(
            nome=nome,
            email=email,
            problema=problema,
            nota=nota,
        )

        suporte = Suporte()
        suporte.suporteCRUD.criarSuporte(novo_suporte)

        print("Suporte cadastrado com sucesso!")
        return 

    def exibir_suporte(self):
        print("----Menu de Suporte----")
        print("Como podemos ajudar?")
        print("(1) Falar com um atendente.")
        print("(2) Voltar ao menu principal.")

        escolha = int(input())

        if escolha == "1":
            Suporte.registrar_suporte()
    