from core.cadastro import Cadastro as cad
from core.consultaService import consultaService as cons
from core.agenda import Agenda as agen
from dataBase.conexao.db_manager import DBManager
class Menus:
    def __init__(self):
        conn, cursor = DBManager.conectar()

        self.opc = None

    def menu_principal(self):
        while True:
            print("----Menu Principal----")
            print("Selecione uma opção para prosseguir:")
            print("(1) Fazer o cadastro.")
            print("(2) Marcar consulta.")
            print("(3) Ver agenda.")
            print("(4) Falar com o suporte.")
            print("(5) Para sair.")

            opcao = input()

            if (not opcao.isdigit() or int(opcao) not in range(1, 6)):
                print("Opção inválida. Digite um número de 1 a 5 para poder continuar.")
                continue

            opcao = int(opcao)

            if (opcao == 1):
                cad.fazer_cadastro()

            elif (opcao == 2):
                cons.agendarConsulta(self)

            elif (opcao == 3):
                agen.exibir_agenda(self)

            elif (opcao == 4):
                Menus().exibir_suporte()

            elif (opcao == 5):
                print("Obrigado por contar o Hospital das Clínicas, espero te ver em breve!!")
                return False


    def exibir_suporte(self):
        print("----Menu de Suporte----")
        print("Como podemos ajudar?")
        print("(1) Falar com um atendente.")
        print("(2) Voltar ao menu principal.")
