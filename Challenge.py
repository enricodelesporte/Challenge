#Lista de pacientes
Pacientes =[]

#Criação do menu principal
def menuPrincipal():
    while Executando:
        print("----Menu Principal----")
        print("Selecione uma opção para prosseguir:")
        print("(1) Fazer o cadastro.")
        print("(2) Marcar consulta.")
        print("(3) Ver agenda.")
        print("(4) Falar com o suporte.")
        print("(5) Para sair.")

        #Escolha do usuário
        opcao = int(input())

        #Válidação da escolha do usuário
        if (not opcao.isdigit() or int(opcao) is range(1, 6)):
            print("Opção inválida. Digite um número de 1 a 5 para poder continuar.")
        
        #Cada opção selecionada criará uma lista no qual será armazenado informações,
        #  isso será util no futuro, principalmente para o banco de dados.
        if (opcao == 1):
            fazerCasatro = []

        elif (opcao == 2):
            marcarConsulta = []
        
        elif (opcao == 3):
            verAgenda = []
        
        elif (opcao == 4):
            suporte = []
        elif (opcao == 5):
            print("Obrigado por contar o Hospital das Clinícas, espero te ver em breve!!")
            executando = False

#Criação da "aba" de cadastro.
def fazerCadastro():
    print("----Cadastro----")
    print("Qual o seu nome completo:")

    #strip é um método usado para remover os possíveis espaços em branco ou não usados, além de remover caracteries especificos 
    # o motivo desse uso é evitar problemas de digitação que o usuário pode cometer, além de evitar problemas na validação de dados nas listas.
    nome = input().strip

    #O uso do while é para evitar que o usuário deixe esse campo em branco, o tornando obrigatório ser preenchido.
    while not nome:
        print("Essse campo deve ser preenchido")
        nome = input().strip
    
    print("Qual o seu CPF (digite apenas número)")
    CPF = int(input())

    #Válidação do CPF, nesse caso válidamos apenas se foi digitado números e se a quantidade digitada está compátivel com um CPF
    while (not CPF.isdigit() or len(CPF) != 11):
        print("Valor informado está errado. Digite um valor de 11 digítos.")
        CPF = int(input())

    print("Digite sua idade:")
    idade = int(input())

    #Valídação da idade do usuário.
    while not idade.isdigit() or int(idade) < 0 or int(idade) > 120:
        print ("Idade inválida. Digite novamente.")
        idade = int(input())
    
    #Adicionando as informações do usuário na lista.
    Pacientes = {"nome": nome, "cpf": CPF, "idade": idade}
    Pacientes.append(Pacientes)
    print ("Paciente ", nome, " cadastrado com sucessso!")

    