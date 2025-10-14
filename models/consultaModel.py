class Consulta:
    def __init__(self, paciente_id, data, hora, especialidade, id):
        self.paciente_id = paciente_id
        self.data = data
        self.hora = hora
        self.especialidade = especialidade
        self.id = id

    def __str__(self):
        return f"Consulta: {self.id}, Data: {self.data}, Hora: {self.hora}, Especialidade: {self.especialidade}"