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
        cep_input = input().strip()
        cep_dados = CEP.buscar_cep(cep_input)

        while not cep_dados:
            print("CEP inválido. Tente novamente:")
            cep_input = input("Qual seu CEP: ").strip()
            cep_dados = CEP.buscar_cep(cep_input)

        cep = cep_dados["cep"]
        

        novo_paciente = Paciente(
            id=id,
            nome=nome,
            idade=idade,
            CPF=cpf,
            email=email,
            senha=senha,
            CEP=cep
        )

        cadastro = Cadastro()
        cadastro.pacienteCRUD.criarPaciente(novo_paciente)

        print("Paciente cadastrado com sucesso!")
        print("------------DADOS CADASTRADOS--------------")
        print("Nome:", nome)
        print("Idade:", idade)
        print("CPF:", cpf)
        print("Email:", email)
        print("Senha:", senha)
        print("CEP:", cep)

        if cep_dados:
            print(f"Endereço: {cep_dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {cep_dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {cep_dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {cep_dados.get('uf', 'Não disponível')}")

        return 