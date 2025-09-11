from dataBase.crud.consultaCRUD import consultaCRUD
from models.consultaModel import Consulta
from dataBase.conexao.db_manager import DBManager
from utils.validacao import Validacao as val


class Agenda:
    def __init__(self):
        conn, cursor = DBManager.conectar()
        
        self.consulta_crud = consultaCRUD(conn)

    def listarConsultas(self):
        return self.consulta_crud.listarConsultas()

    def exibir_agenda(self):
        consultas = consultaCRUD.listarConsultas(self)

        print("\n----  Agenda de Consultas ----")
        print("Qual seu nome:")
        paciente = val.validar_usuario(input())

        if paciente is None:
            print("Paciente não cadastrado. Voltando ao menu principal...")
            return 
        
        if not consultas:
            print("Nenhuma consulta agendada no momento.")
        else:
            for cons in consultas:
                if isinstance(cons, Consulta):
                    print(f"Paciente: {cons.paciente_id} | "
                          f"Especialidade: {cons.especialidade} | "
                          f"Data: {cons.data} | Hora: {cons.hora}")
                else:
                    print(f"ID: {cons[0]} | Paciente: {cons[1]} | "
                          f"Especialidade: {cons[2]} | "
                          f"Data: {cons[3]} | Hora: {cons[4]}")

        print("\n(1) Voltar ao menu")