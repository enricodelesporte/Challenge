from models.pacienteModel import Paciente
from dataBase.crud.pacienteCRUD import pacienteCRUD
from utils.validacao import Validacao as val
from dataBase.conexao.db_manager import DBManager
from utils.api_cep import ViaCEP as CEP

class Cadastro:
    def __init__(self):
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
        print("Qual seu CEP:")
        cep = CEP.buscar_cep(input())   
        while not cep:
            print("Por favor, insira um CEP válido:")
            cep = CEP.buscar_cep(input())
        

        novo_paciente = Paciente(
            id=id,
            nome=nome,
            idade=idade,
            CPF=cpf,
            email=email,
            senha=senha
        )

        cadastro = Cadastro()
        cadastro.pacienteCRUD.criarPaciente(novo_paciente)

        print("Paciente cadastrado com sucesso!")

        return 