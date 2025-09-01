from models.pacienteModel import Paciente
from dataBase.crud.pacienteCRUD import pacienteCRUD
from utils.validacao import Validacao as val
from dataBase.conexao.oracleConexao import oracleConexao


class cadastro:
    def __init__(self, nome: str, idade: int, CPF: str, email: str, senha: str):
        paciente = Paciente(nome, idade, CPF, email, senha)
        conexao = oracleConexao(
            user="rm565760",
            password="150606",
            host="localhost",
            port="1521",
            serviceName="orcl"
        )
        conn, cursor = conexao.conectar()
        paciente_crud = pacienteCRUD(conexao)
        paciente_crud.criarPaciente(paciente=paciente)
        conexao.desconectar(conn, cursor)
        return paciente

    @staticmethod
    def fazer_cadastro():
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
        
