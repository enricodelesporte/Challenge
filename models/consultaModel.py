class Consulta:
    def __init__(self, paciente, data, hora, especialidade):
        self.paciente = paciente
        self.data = data
        self.hora = hora
        self.especialidade = especialidade

    def __str__(self):
        return f"Consulta: {self.paciente}, Data: {self.data}, Hora: {self.hora}, Especialidade: {self.especialidade}"