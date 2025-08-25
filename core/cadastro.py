from models.pacienteModel import Paciente
from dataBase import pacienteCRUD

class cadastro:
    def __init__(self, nome: str, idade: int, CPF: str):
        paciente = Paciente(nome, idade, CPF)
        pacienteCRUD.adicionar_paciente(paciente)
        return paciente