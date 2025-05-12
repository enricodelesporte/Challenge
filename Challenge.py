import datetime
#Lista de pacientes
Pacientes =[]
Consultas = []
Agenda = []

Executando = True


#Criação do menu principal
def menuPrincipal():
    global Executando
    while Executando:
        print("----Menu Principal----")
        print("Selecione uma opção para prosseguir:")
        print("(1) Fazer o cadastro.")
        print("(2) Marcar consulta.")
        print("(3) Ver agenda.")
        print("(4) Falar com o suporte.")
        print("(5) Para sair.")

        #Escolha do usuário
        opcao = input()
        
        #Válidação da escolha do usuário
        if (not opcao.isdigit() or int(opcao) not in range(1, 6)):
            print("Opção inválida. Digite um número de 1 a 5 para poder continuar.")
            continue
        
        #Cada opção selecionada criará uma lista no qual será armazenado informações,
        #  isso será util no futuro, principalmente para o banco de dados.
        opcao = int(opcao)

        if (opcao == 1):
            fazerCadastro()

        elif (opcao == 2):
            marcarConsulta()
        
        elif (opcao == 3):
            verAgenda()
        
        elif (opcao == 4):
            suporte()
        elif (opcao == 5):
            print("Obrigado por contar o Hospital das Clínicas, espero te ver em breve!!")
            Executando = False
        

#Criação da "aba" de cadastro.
def fazerCadastro():
    print("----Cadastro----")
    print("Qual o seu nome completo:")

    #FAZER VALIDAÇÃO DO NOME

    #strip é um método usado para remover os possíveis espaços em branco ou não usados, além de remover caracteries especificos 
    # o motivo desse uso é evitar problemas de digitação que o usuário pode cometer, além de evitar problemas na validação de dados nas listas.
    nome = input().strip

    #O uso do while é para evitar que o usuário deixe esse campo em branco, o tornando obrigatório ser preenchido.
    while not nome:
        print("Essse campo deve ser preenchido")
        nome = input().strip()
    
    print("Qual o seu CPF (digite apenas número)")
    CPF = input()

    #Válidação do CPF, nesse caso válidamos apenas se foi digitado números e se a quantidade digitada está compátivel com um CPF
    while (not CPF.isdigit() or len(CPF) != 11):
        print("Valor informado está errado. Digite um valor de 11 digítos.")
        CPF = input()

    print("Digite sua idade:")
    idade = input()


    #Valídação da idade do usuário.
    while (not idade.isdigit() or int(idade) < 16 or int(idade) > 120):
        print ("Idade inválida. Digite novamente.")
        idade = input()
    
    #Adicionando as informações do usuário na lista.
    Paciente = {"nome": nome, "cpf": CPF, "idade": idade}
    Pacientes.append(Paciente)
    print ("Paciente", nome, "cadastrado com sucessso!")

#Criação da "aba" de marcar consulta.
def marcarConsulta():

    #PERGUNTAR NOME PARA SABER SE O PACIENTE JÁ ESTA CADASTRADO E FAZER A VALIDAÇÃO

    #Valídação para saber se o paciente se cadastrou.
    if (not Pacientes):
        print("Nenhum paciente cadastrado, faça seu cadastro primeiro.")
        return
    
    #Verificação se o paciente está registrado no sistema
    print("Digite seu nome para verificar o seu cadastro:")
    nome = input().strip()

    pacienteEncontrado = False
    for paciente in Pacientes:
        if paciente["nome"].lower() == nome.lower():
            pacienteEncontrado = True
            break
    if not pacienteEncontrado:
        print("Paciente não encontrado. Verifique se digitou corretamente ou faça seu cadastro primeiro.")
        return

    #Interação com o usuário
    print("Qual médico especialista você deseja marcar:")
    especialidade = input().strip()
    print("Qual data deseja marcar sua consult (dd/MM):")
    data = input().strip()
    print("Qual horário deseja marcar?")
    horario = input()
    print("Consulta maracada para o dia ", data, "ás", horario, "para uma consulta sobre ", especialidade, ".")

    #Criação da lista de consulta
    Consulta = {"especialidade": especialidade, "data": data}
    Consulta.append(Consulta)
    print("Consulta marcada com sucesso!")

#Criação da "aba" de Agenda
def verAgenda():
    print("----Agenda----")

    #Validação para saber se alguma consulta já foi marcada.
    if (not Consultas):
        print("Nenhuma consulta marcada!")
    #Abaixo foi feito um teste, caso tenha consulta maracada, seria pego cada uma, começando do 1 (devido ao "start = 1")
    # Para cada consulta ele começa com o númeiro "i", para enumerar a lista da agenda, mostrando as informações de data, hora, nome e especialidade. 
    else: 
        for i, Consulta in enumerate(Consultas, start=1):
            print(f"{i}.Paciente: {Consulta['nome']}, Data: {Consulta['data']}, Horário: {Consulta['horario']}, Especialidade: {Consulta['especialidade']}")
        print()

#Criação da "aba" de Suporte.
def suporte():
    print("----Suporte----")
    print("Descreva o problema:")
    problema = input().strip()
    if (problema):
        print("Sua mensagem foi enviada para o nosso suporte.")
    else:
        print("Este campo está vazio. Prencha corretamente.")

menuPrincipal()