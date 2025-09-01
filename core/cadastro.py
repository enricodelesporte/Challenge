from models.pacienteModel import Paciente
from dataBase.crud.pacienteCRUD import pacienteCRUD

class cadastro:
    def __init__(self, nome: str, idade: int, CPF: str, email: str, senha: str):

        paciente = Paciente(nome, idade, CPF, email, senha)
        pacienteCRUD.criarPaciente(paciente= paciente)
        return paciente  