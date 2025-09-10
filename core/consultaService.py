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

    def agendarConsulta(self):
        vali = val.Validacao()

        print("----Menu de Consulta----")
        nome_paciente = input("Qual o nome do paciente: ").strip()
        paciente = vali.validar_usuario(nome_paciente)

        if paciente is None:
            print("Paciente não cadastrado. Voltando ao menu principal...")
            return  # volta ao menu sem prosseguir

        especialidade = vali.validar_especialidade(input("Qual a especialidade médica: "))
        data = vali.validar_data(input("Qual a data da consulta: "))
        hora = vali.validar_hora(input("Qual o horário da consulta: "))

        nova_consulta = Consulta(
            paciente=paciente,            
            especialidade=especialidade,
            data=data,
            hora=hora
        )

        consulta = consultaService()
        consulta.consultaCRUD.criarConsulta(nova_consulta)

        print("Consulta agendada com sucesso!")

    def listarConsultas(self):
        return self.consultaCRUD.listarConsultas()

    def cancelarConsulta(self, idConsulta):
        self.consultaCRUD.deletarConsulta(idConsulta)
        print("Consulta cancelada com sucesso!")