from models.pacienteModel import Paciente
from dataBase.crud.pacienteCRUD import pacienteCRUD
from utils.validacao import Validacao as val
from dataBase.conexao.oracleConexao import oracleConexao


class cadastro:
    def __init__(self, nome: str, idade: int, CPF: str, email: str, senha: str):
        self.paciente = Paciente(nome, idade, CPF, email, senha)
        conexao = oracleConexao(
            user="rm565760",
            password="150606",
            host="oracle.fiap.com.br",
            port="1521",
            serviceName="orcl"
        )
        conn, cursor = conexao.conectar()
        if conn and cursor:
            paciente_crud = pacienteCRUD(conn)
            paciente_crud.criarTabelaPaciente()  # Criar tabela se não existir
            paciente_crud.criarPaciente(paciente=self.paciente)
            print("Paciente cadastrado com sucesso!")
        else:
            print("Erro ao conectar com o banco de dados!")
        conexao.desconectar(conn, cursor)

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
        
