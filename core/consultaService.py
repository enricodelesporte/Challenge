from models.consultaModel import Consulta
from dataBase.crud.consultaCRUD import consultaCRUD
from utils import validacao as val
from dataBase.conexao.oracleConexao import oracleConexao


class consultaService:
    def __init__(self):
        self.conexao = oracleConexao(
            user="rm565760",
            password="150606",
            host="oracle.fiap.com.br",
            port="1521",
            serviceName="orcl"
        )
        self.conn = self.conexao.conectar()
        if self.conn:
            self.consultaCRUD = consultaCRUD()
            self.consultaCRUD.criarTabelaConsulta()
        else:
            print("Erro ao conectar com o banco de dados!")
            self.consultaCRUD = None

    def exibir_consulta(self):
        if not self.consultaCRUD:
            print("Banco indisponível.")
            return
        print("----Consultas----")
        print(f"{'Paciente':<20} {'Data':<15} {'Hora':<10} {'Especialidade':<15}")
        for consulta in self.listarConsultas():
            print(f"{consulta.paciente:<20} {consulta.data:<15} {consulta.hora:<10} {consulta.especialidade:<15}")

    def agendarConsulta(self):
        if not self.consultaCRUD:
            print("Banco indisponível.")
            return

        vali = val.Validacao()

        print("----Menu de Consulta----")
        print("Qual o nome do paciente: ")
        paciente = vali.validar_usuario(input())
        print("Qual a especialidade médica: ")
        especialidade = vali.validar_especialidade(input())
        print("Qual a data da consulta: ")
        data = vali.validar_data(input())
        print("Qual o horário da consulta: ")
        hora = vali.validar_hora(input())

        consulta = Consulta(paciente=paciente, especialidade=especialidade, data=data, hora=hora)
        self.consultaCRUD.criarConsulta(consulta)
        print("Consulta agendada com sucesso!")

    def listarConsultas(self):
        if not self.consultaCRUD:
            return []
        return self.consultaCRUD.listarConsultas()

    def cancelarConsulta(self, idConsulta):
        if not self.consultaCRUD:
            print("Banco indisponível.")
            return
        self.consultaCRUD.deletarConsulta(idConsulta)

    def fechar(self):
        self.conexao.desconectar()