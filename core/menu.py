class menu:
    def __init__(self, opcao):
        self.opcao = opcao

    def __str__(self):
        return("----Menu Principal----\n"
               "Selecione uma opção para prosseguir:\n"
               "(1) Fazer o cadastro.\n"
               "(2) Marcar consulta.\n"
               "(3) Ver agenda.\n"
               "(4) Falar com o suporte.\n"
               "(5) Para sair.")

        print("(5) Para sair.")