from models.consultaModel import Consulta
from dataBase.crud.consultaCRUD import consultaCRUD

class consultaService:
    def __init__(self):
        self.consultaCRUD = consultaCRUD()

    def agendarConsulta(self, idPaciente, idConsulta, data, hora, especialidade):
        consulta = Consulta(paciente_id=idPaciente, data=data, hora=hora, especialidade=especialidade, consulta_id=idConsulta)
        self.consultaCRUD.criarConsulta(consulta)
        return consulta
    
    def listarConsultas(self):
        return self.consultaCRUD.listarConsultas()

    def cancelarConsulta(self, idConsulta):
        self.consultaCRUD.deletarConsulta(idConsulta)