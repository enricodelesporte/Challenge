from core.cadastro import cadastro as cad
class Menus:
    def __init__(self):
        self.opc = None

    def menu_principal(self):
        print("----Menu Principal----")
        print("Selecione uma opção para prosseguir:")
        print("(1) Fazer o cadastro.")
        print("(2) Marcar consulta.")
        print("(3) Ver agenda.")
        print("(4) Falar com o suporte.")
        print("(5) Para sair.")

        while True:
            opcao = input()

            if (not opcao.isdigit() or int(opcao) not in range(1, 6)):
                print("Opção inválida. Digite um número de 1 a 5 para poder continuar.")
                continue

            opcao = int(opcao)

            if (opcao == 1):
                cad.fazer_cadastro()

            elif (opcao == 2):
                Menus().exibir_consulta()

            elif (opcao == 3):
                Menus().exibir_agenda()

            elif (opcao == 4):
                Menus().exibir_suporte()

            elif (opcao == 5):
                print("Obrigado por contar o Hospital das Clínicas, espero te ver em breve!!")
                return False
    

    def exibir_consulta(self):
        print("----Menu de Consulta----")
        print("Qual o nome do paciente:")
        print("Qual a especialidade médica:")
        print("Qual a data da consulta:")
        print("Qual o horário da consulta:")
        print("(1) Voltar.")


    def exibir_agenda(self):
        print("----Menu de Agenda----")
        print("Aqui estão suas consultas agendadas:")
        print("(1) Voltar.")


    def exibir_suporte(self):
        print("----Menu de Suporte----")
        print("Como podemos ajudar?")
        print("(1) Falar com um atendente.")
        print("(2) Voltar ao menu principal.")
