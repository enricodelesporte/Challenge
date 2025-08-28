from models.pacienteModel import Paciente
from dataBase import pacienteCRUD

class cadastro:
    def __init__(self, nome: str, idade: int, CPF: str, email: str):
        paciente = Paciente(nome, idade, CPF, email)
        pacienteCRUD.adicionar_paciente(paciente)
        return paciente  