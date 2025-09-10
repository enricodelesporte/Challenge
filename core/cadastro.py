from models.pacienteModel import Paciente
from dataBase.crud.pacienteCRUD import pacienteCRUD
from utils.validacao import Validacao as val
from dataBase.conexao.db_manager import DBManager


class Cadastro:
    def __init__(self):
        # Pega a conexão pelo DBManager
        conn, cursor = DBManager.conectar()
        self.pacienteCRUD = pacienteCRUD(conn)
        self.pacienteCRUD.criarTabelaPaciente()

    @staticmethod
    def fazer_cadastro():
        vali = val()

        print("---- Menu de Cadastro ----")
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

        novo_paciente = Paciente(
            nome=nome,
            idade=idade,
            CPF=cpf,
            email=email,
            senha=senha
        )

        cadastro = Cadastro()
        cadastro.pacienteCRUD.criarPaciente(novo_paciente)

        print("Paciente cadastrado com sucesso!")