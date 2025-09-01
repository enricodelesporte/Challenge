from core.cadastro import cadastro as cad
from utils.validacao import Validacao


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

    def exibir_cadastro(self):
        vali = Validacao()

        print("----Menu de Cadastro----")
        print("Qual seu nome:")
        nome = vali.validar_nome(input())
        print("Qual sua idade:")
        idade = vali.validar_criar_conta_idade(input())
        print("Qual seu CPF:")
        cpf = vali.validar_criar_conta_cpf(input())
        print("Qual seu email:")
        email = vali.validar_email(input())
        print("Qual sua senha:")
        senha = vali.validar_criar_conta_senha(input())
        print("(1) Voltar.")

        

        cad(nome= nome, idade= idade, CPF= cpf, email= email, senha = senha)


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
