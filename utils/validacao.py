from models.agendaModel import Agenda
from models.pacienteModel import Paciente
from models.consultaModel import Consulta

from dataBase.crud.pacienteCRUD import pacienteCRUD
from dataBase.crud.consultaCRUD import consultaCRUD

class Validacao:
    
    def validar_criar_conta_senha(self, senha):
        while not senha or len(senha) <= 5:
            if not senha:
                print("Senha inválida. A senha não pode estar vazia.")
            elif len(senha) <= 5:
                print("Senha fraca. A senha deve ter pelo menos 6 caracteres.")
                senha = input("Digite a senha novamente: ")
        return senha

    def validar_criar_conta_cpf(self, cpf):
        while not cpf or len(cpf) != 11 or not cpf.isdigit():
            if not cpf:
                print("CPF inválido. O CPF não pode estar vazio.")
            elif len(cpf) != 11:
                print("CPF inválido. O CPF deve ter 11 dígitos.")
                cpf = input("Digite o CPF novamente: ")
        return cpf
    
    def validar_criar_conta_idade(self, idade):
        while not idade or not idade.isdigit() or int(idade) <= 16 or int(idade) >= 120:
            if not idade:
                print("Idade inválida. A idade não pode estar vazia.")
            elif not idade.isdigit():
                print("Idade inválida. A idade deve ser um número.")
            elif int(idade) <= 16 or int(idade) >= 120:
                print("Idade inválida. A idade deve ser maior que 15 anos.")
            idade = input("Digite a idade novamente: ")
        return idade
    
    def validar_nome(self, nome):
        while not nome or len(nome) < 3:
            print("Nome inválido. O nome deve ter pelo menos 2 caracteres.")
            nome = input("Digite o nome novamente: ")
        return nome

    def validar_email(self, email):
        while not email or "@" not in email or "." not in email:
            print("Email inválido.")
            email = input("Digite o email novamente: ")
        return email

    def validar_cpf(self, cpf):
        while not cpf or len(cpf) != 11 or not cpf.isdigit():
            if not cpf:
                print("CPF inválido. O CPF não pode estar vazio.")
            elif len(cpf) != 11:
                print("CPF inválido. O CPF deve ter 11 dígitos.")
            elif not cpf.isdigit():
                print("CPF inválido. O CPF deve conter apenas dígitos.")
            cpf = input("Digite o CPF novamente: ")
        return cpf

    def validar_login_cpf(self, cpf):
        pacientes = pacienteCRUD.listar_pacientes()

        while not cpf or not any(p.cpf == cpf for p in pacientes):
            if not cpf:
                print("CPF inválido. O CPF não pode estar vazio.")
            elif not any(p.cpf == cpf for p in pacientes):
                print("CPF inválido. O CPF não corresponde a nenhum paciente cadastrado.")
            cpf = input("Digite o CPF novamente: ")
        return cpf
    
    def validar_login_senha(self, senha):
        pacientes = pacienteCRUD.listar_pacientes()

        while not senha or len(senha) <= 7 or not any(p.senha == senha for p in pacientes):
            if not senha:
                print("Senha inválida. A senha não pode estar vazia.")
            elif len(senha) <= 7:
                print("Senha fraca. A senha deve ter pelo menos 8 caracteres.")
            elif not any(p.senha == senha for p in pacientes):
                print("Senha incorreta. Tente novamente.")
        return senha

    def validar_usuario(self, usuario : Paciente):
        pacientes = pacienteCRUD.listar_pacientes()

        if not any(p.nome == usuario.nome for p in pacientes):
            print("Usuário não encontrado. Faça seu cadastro primeiro.")
            return usuario
        
        print("Usuário não encontrado. Faça seu cadastro primeiro.")
        return False

    def validar_consulta(self, consulta: Consulta):
        while consulta not in consultaCRUD.listar_consultas():
            print("Consulta não encontrada. Verifique se foi marcada corretamente.")
            return False
        return consulta

    def validar_agenda(self, agenda: Agenda, consulta: Consulta):
        while consulta not in agenda.consultas:
            print("Consulta não encontrada na agenda. Verifique se foi marcada corretamente.")
            return False
        return agenda
    