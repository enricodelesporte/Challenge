from dataBase.crud.consultaCRUD import consultaCRUD
from models.consultaModel import Consulta
class Agenda:
    def __init__(self, conexao):
        self.crud = consultaCRUD(conexao)

    def criarConsulta(self, consulta: Consulta):
        self.crud.criarConsulta(consulta)

    def listarConsultas(self):
        return self.crud.listarConsultas()

    def atualizarConsulta(self, idConsulta, novaData, novoHorario):
        self.crud.atualizarConsulta(idConsulta, novaData, novoHorario)

    def deletarConsulta(self, idConsulta):
        self.crud.deletarConsulta(idConsulta)