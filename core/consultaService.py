from models.consultaModel import Consulta
from dataBase.crud.consultaCRUD import consultaCRUD
from utils import validacao as val
from dataBase.conexao.db_manager import DBManager

class consultaService:
    def __init__(self):
        # Pega a conexão e cursor do DBManager
        conn, cursor = DBManager.conectar()
        
        # Instancia o CRUD com a conexão
        self.consultaCRUD = consultaCRUD(conn)
        self.consultaCRUD.criarTabelaConsulta()

    def exibir_consulta(self):
        print("---- Consultas ----")
        print(f"{'ID':<5} {'Paciente':<20} {'Data':<15} {'Hora':<10} {'Especialidade':<15}")
        for consulta in self.listarConsultas():
            print(f"{consulta.id:<5} {consulta.paciente:<20} {consulta.data:<15} {consulta.hora:<10} {consulta.especialidade:<15}")

    def agendarConsulta():
        vali = val.Validacao()

        print("---- Menu de Consulta ----")
        print("Qual o nome do paciente:")
        paciente = vali.validar_usuario(input())
        print("Qual a especialidade médica:")
        especialidade = vali.validar_especialidade(input())
        print("Qual a data da consulta:")
        data = vali.validar_data(input())
        print("Qual o horário da consulta:")
        hora = vali.validar_hora(input())
        print("(1) Voltar.")

        nova_consulta = Consulta(
            paciente=paciente,
            especialidade=especialidade,
            data=data,
            hora=hora
        )

        self.consultaCRUD.criarConsulta(nova_consulta)
        print("Consulta agendada com sucesso!")

    def listarConsultas(self):
        return self.consultaCRUD.listarConsultas()

    def cancelarConsulta(self, idConsulta):
        self.consultaCRUD.deletarConsulta(idConsulta)
        print("Consulta cancelada com sucesso!")