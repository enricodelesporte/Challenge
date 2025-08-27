class Suporte:
    def __init__(self, nome: str, problema: str, email: str, nota: str = None):
        self.nome = nome
        self.problema = problema
        self.email = email
        self.nota = nota

    def __str__(self):
        return f"Obrigado por entrar em contato, {self.nome}. Seu problema foi registrado e retornaremos em contato em breve, através do email: {self.email}"