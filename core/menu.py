class Menu:
    def __init__(self, opcao):
        self.opcao = opcao

    def menu_principal(self):
        print("----Menu Principal----")
        print("Selecione uma opção para prosseguir:")
        print("(1) Fazer o cadastro.")
        print("(2) Marcar consulta.")
        print("(3) Ver agenda.")
        print("(4) Falar com o suporte.")
        print("(5) Para sair.")

    def menu_cadastro(self):
        print("----Menu de Cadastro----")
        print("Qual seu nome:")
        print("Qual sua idade:")
        print("Qual seu CPF:")
        print("(1) Voltar.")

    def menu_consulta(self):
        print("----Menu de Consulta----")
        print("Qual o nome do paciente:")
        print("Qual a especialidade médica:")
        print("Qual a data da consulta:")
        print("Qual o horário da consulta:")
        print("(1) Voltar.")

    def menu_agenda(self):
        print("----Menu de Agenda----")
        print("Aqui estão suas consultas agendadas:")
        print("(1) Voltar.")

    def menu_suporte(self):
        print("----Menu de Suporte----")
        print("Como podemos ajudar?")
        print("(1) Falar com um atendente.")
        print("(2) Voltar ao menu principal.")