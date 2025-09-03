from models.consultaModel import Consulta
from dataBase.crud.consultaCRUD import consultaCRUD
from utils import validacao as val
from dataBase.conexao.oracleConexao import oracleConexao

class consultaService:
    def __init__(self, paciente, especialidade, data, hora):
        conexao = oracleConexao(
            user="rm565760",
            password="150606",
            host="oracle.fiap.com.br",
            port="1521",
            serviceName="orcl"
        )
        conn, cursor = conexao.conectar()

        if conn and cursor:
            consulta_crud = consultaCRUD(conn)  # passa só o conn
            consulta_crud.criarTabelaConsulta()
            consulta_crud.criarConsulta(
                consulta=Consulta(
                    paciente=paciente,
                    especialidade=especialidade,
                    data=data,
                    hora=hora
                )
            )
            print("Consulta agendada com sucesso!")
        else:
            print("Erro ao conectar com o banco de dados!")

        conexao.desconectar(conn, cursor)

    def exibir_consulta(self):
        print("----Consultas----")
        print(f"{'ID':<5} {'Paciente':<20} {'Data':<15} {'Hora':<10} {'Especialidade':<15}")
        for consulta in self.listarConsultas():
            print(f"{consulta.id:<5} {consulta.paciente:<20} {consulta.data:<15} {consulta.hora:<10} {consulta.especialidade:<15}")

    @staticmethod
    def agendarConsulta():
        vali = val.Validacao()

        print("----Menu de Consulta----")
        print("Qual o nome do paciente:")
        paciente = vali.validar_usuario(input())
        print("Qual a especialidade médica:")
        especialidade = vali.validar_especialidade(input())
        print("Qual a data da consulta:")
        data = vali.validar_data(input())
        print("Qual o horário da consulta:")
        hora = vali.validar_hora(input())
        print("(1) Voltar.")

        consultaService(paciente=paciente, especialidade=especialidade, data=data, hora=hora)

    def listarConsultas(self):
        conexao = oracleConexao(
            user="rm565760",
            password="150606",
            host="oracle.fiap.com.br",
            port="1521",
            serviceName="orcl"
        )
        conn, cursor = conexao.conectar()
        consultas = []

        if conn and cursor:
            consulta_crud = consultaCRUD(conn)
            consultas = consulta_crud.listarConsultas()
        else:
            print("Erro ao conectar com o banco de dados!")

        conexao.desconectar(conn, cursor)
        return consultas

    def cancelarConsulta(self, idConsulta):
        conexao = oracleConexao(
            user="rm565760",
            password="150606",
            host="oracle.fiap.com.br",
            port="1521",
            serviceName="orcl"
        )
        conn, cursor = conexao.conectar()

        if conn and cursor:
            consulta_crud = consultaCRUD(conn)
            consulta_crud.deletarConsulta(idConsulta)
        else:
            print("Erro ao conectar com o banco de dados!")

        conexao.desconectar(conn, cursor)