class SuporteModel:
    def __init__(self, nome: str, email: str, problema: str, nota: int):
        self.nome = nome
        self.email = email
        self.problema = problema
        self.nota = nota

    def __str__(self):
        return f"Obrigado por entrar em contato, {self.nome}. Seu problema foi registrado e retornaremos em contato em breve, através do email: {self.email}"