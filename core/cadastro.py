from models.pacienteModel import Paciente
from dataBase.crud.pacienteCRUD import pacienteCRUD
from utils.validacao import Validacao as val


class cadastro:
    def __init__(self, nome: str, idade: int, CPF: str, email: str, senha: str):

        paciente = Paciente(nome, idade, CPF, email, senha)
        pacienteCRUD.criarPaciente(paciente= paciente)
        return paciente

    def fazer_cadastro(self):
        vali = val()
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

        cadastro(nome= nome, idade= idade, CPF= cpf, email= email, senha = senha)
        
